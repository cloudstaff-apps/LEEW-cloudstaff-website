#!/usr/bin/env python3
"""
Post-build noindex injector for the PROTOTYPE static site (docs/ only).

Run after the build:

    python3 build.py && python3 tools/noindex.py

What it does
  1. Inserts one robots meta tag into the <head> of every HTML page under
     docs/, so search engines do not index the GitHub Pages prototype.
  2. Scans wordpress/cloudstaff-theme/ and fails (exit 1) if any noindex
     directive has leaked into the theme. The theme is destined for the live
     site and must stay indexable.

Flags
  --dry-run   report what would change, write nothing
  --check     write nothing; exit 1 unless every docs/ page already has the
              tag and the WordPress theme is clean

Idempotent: any existing robots meta tag is replaced, never duplicated.
A robots.txt is deliberately not used. The site publishes to a subpath of
github.io, and crawlers only consult robots.txt at the host root.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
THEME = os.path.join(ROOT, "wordpress", "cloudstaff-theme")

TAG = '<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">'
ROBOTS_RE = re.compile(r'[ \t]*<meta\s+name=["\']robots["\'][^>]*>[ \t]*\r?\n?', re.I)
ANCHOR_RE = re.compile(r'(<meta\s+name=["\']viewport["\'][^>]*>[ \t]*\r?\n)', re.I)
HEAD_RE = re.compile(r'(<head[^>]*>[ \t]*\r?\n?)', re.I)
LEAK_RE = re.compile(r'noindex|name=["\']robots["\']|X-Robots-Tag', re.I)
THEME_EXT = (".php", ".html", ".htm", ".js", ".json", ".txt")


def html_files(base):
    for dirpath, _dirs, files in os.walk(base):
        for name in sorted(files):
            if name.lower().endswith((".html", ".htm")):
                yield os.path.join(dirpath, name)


def inject(text):
    """Return text with exactly one robots tag in <head>, or None if no <head>."""
    stripped = ROBOTS_RE.sub("", text)
    if ANCHOR_RE.search(stripped):
        return ANCHOR_RE.sub(lambda m: m.group(1) + TAG + "\n", stripped, count=1)
    if HEAD_RE.search(stripped):
        return HEAD_RE.sub(lambda m: m.group(1) + TAG + "\n", stripped, count=1)
    return None


def theme_leaks():
    leaks = []
    if not os.path.isdir(THEME):
        return leaks
    for dirpath, _dirs, files in os.walk(THEME):
        for name in sorted(files):
            if not name.lower().endswith(THEME_EXT):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8", errors="replace") as f:
                for n, line in enumerate(f, 1):
                    if LEAK_RE.search(line):
                        leaks.append(f"{os.path.relpath(path, ROOT)}:{n}")
    return leaks


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    write = not (args.dry_run or args.check)

    files = list(html_files(DOCS))
    if not files:
        print("noindex: no HTML files found in docs/. Run build.py first.")
        return 1

    changed, ok, failed = [], [], []
    for path in files:
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        new = inject(text)
        if new is None:
            failed.append(rel)
        elif new == text:
            ok.append(rel)
        else:
            changed.append(rel)
            if write:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new)

    verb = "tagged" if write else "needs tag"
    for rel in changed:
        print(f"noindex: {verb}: {rel}")
    for rel in failed:
        print(f"noindex: ERROR no <head> found: {rel}")
    print(f"noindex: docs/ pages: {len(files)} total, {len(ok)} already tagged, "
          f"{len(changed)} {verb}, {len(failed)} failed")

    leaks = theme_leaks()
    if leaks:
        print("noindex: ERROR noindex leaked into the WordPress theme:")
        for leak in leaks:
            print(f"  {leak}")
    else:
        print("noindex: WordPress theme is clean (no noindex directives)")

    if failed or leaks:
        return 1
    if args.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
