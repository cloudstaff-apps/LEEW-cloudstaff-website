#!/usr/bin/env python3
"""
Build script: generates the static preview site (docs/) and the WordPress
theme page templates (wordpress/cloudstaff-theme/) from one set of shared
content partials in src/partials/.

Single source of truth:
  src/partials/<slug>.html   page body (lander markup, design-system classes)
  src/header.html            shared site header (topbar)
  src/footer.html            shared site footer
  src/site.css               small custom CSS layer (tokens only)
  src/meta.json              page titles, descriptions, nav config

Placeholders understood inside partials/header/footer:
  {{URL:<slug>}}     -> static: "<slug>.html" ("index.html" for home)
                        wordpress: "/" or "/<slug>/"
  {{ACTIVE:<slug>}}  -> aria-current="page" when building that page (static)
                        php conditional (wordpress)
"""
import json, os, re, shutil, html, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from icons import FA_MAP, icon_svg, hero_art, logo, cert_seal, flag  # noqa: E402
SRC = os.path.join(ROOT, "src")
DOCS = os.path.join(ROOT, "docs")
THEME = os.path.join(ROOT, "wordpress", "cloudstaff-theme")

meta = json.load(open(os.path.join(SRC, "meta.json")))
CDN = meta["site"]["cdn"]
pages = {p["slug"]: p for p in meta["pages"]}

# Screenshots and other images in src/ that pages reference with {{ASSET:name}}.
IMAGES = ["coworker-profile.png", "coworker-team.png"]

read = lambda *p: open(os.path.join(*p), encoding="utf-8").read()
header_tpl = read(SRC, "header.html")
footer_tpl = read(SRC, "footer.html")


def sub_common(text):
    """Shared substitutions: inline SVG icons, hero art, logo."""
    def icon(m):
        name = "fa-" + m.group(1)
        if name not in FA_MAP:
            raise KeyError(f"No glyph mapped for {name}")
        return icon_svg(FA_MAP[name])
    text = re.sub(r'<i class="fa-light fa-([a-z0-9-]+)"[^>]*></i>', icon, text)
    text = re.sub(r"\{\{ART:([a-z0-9-]+)\}\}", lambda m: hero_art(m.group(1)), text)
    text = re.sub(r"\{\{SEAL:([a-z0-9]+)\}\}", lambda m: cert_seal(m.group(1)), text)
    text = re.sub(r"\{\{FLAG:([a-z]{2})\}\}", lambda m: flag(m.group(1)), text)
    text = text.replace("{{LOGO:light}}", logo("light")).replace("{{LOGO}}", logo())
    return text


def sub_static(text, current_slug):
    text = sub_common(text)
    text = re.sub(r"\{\{ASSET:([a-z0-9.-]+)\}\}", lambda m: "assets/" + m.group(1), text)
    def url(m):
        slug = m.group(1)
        return "index.html" if slug == "index" else f"{slug}.html"
    text = re.sub(r"\{\{URL:([a-z0-9-]+)\}\}", url, text)
    def active(m):
        return 'aria-current="page"' if m.group(1) == current_slug else ""
    text = re.sub(r"\{\{ACTIVE:([a-z0-9-]+)\}\}", active, text)
    return text


def sub_wp(text):
    text = sub_common(text)
    text = re.sub(r"\{\{ASSET:([a-z0-9.-]+)\}\}", lambda m: "<?php echo esc_url( get_template_directory_uri() . '/" + m.group(1) + "' ); ?>", text)
    def url(m):
        slug = m.group(1)
        path = "/" if slug == "index" else f"/{slug}/"
        return f"<?php echo esc_url( home_url( '{path}' ) ); ?>"
    text = re.sub(r"\{\{URL:([a-z0-9-]+)\}\}", url, text)
    def active(m):
        slug = m.group(1)
        return (f"<?php if ( is_page( '{slug}' ) ) echo 'aria-current=\"page\"'; ?>")
    text = re.sub(r"\{\{ACTIVE:([a-z0-9-]+)\}\}", active, text)
    return text


STATIC_SHELL = """<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="{cdn}/fonts/fonts.css">
<link rel="stylesheet" href="{cdn}/css/ui.min.css">
<link rel="stylesheet" href="assets/site.css">
<script src="{cdn}/css/ui.min.js" defer></script>
</head>
<body>
{header}
<main class="site-main" id="main-content">
{body}
</main>
{footer}
</body>
</html>
"""


def build_static():
    os.makedirs(os.path.join(DOCS, "assets"), exist_ok=True)
    shutil.copyfile(os.path.join(SRC, "site.css"), os.path.join(DOCS, "assets", "site.css"))
    shutil.copyfile(os.path.join(SRC, "teambuilder.js"), os.path.join(DOCS, "assets", "teambuilder.js"))
    shutil.copyfile(os.path.join(SRC, "coverage.js"), os.path.join(DOCS, "assets", "coverage.js"))
    shutil.copyfile(os.path.join(SRC, "coworkers.js"), os.path.join(DOCS, "assets", "coworkers.js"))
    shutil.copyfile(os.path.join(SRC, "cloudstaff-logo.png"), os.path.join(DOCS, "assets", "cloudstaff-logo.png"))
    shutil.copyfile(os.path.join(SRC, "cloudstaff-logo-light.png"), os.path.join(DOCS, "assets", "cloudstaff-logo-light.png"))
    for img in IMAGES:
        shutil.copyfile(os.path.join(SRC, img), os.path.join(DOCS, "assets", img))
    open(os.path.join(DOCS, ".nojekyll"), "w").close()
    for slug, p in pages.items():
        body = read(SRC, "partials", f"{slug}.html")
        page_html = STATIC_SHELL.format(
            title=html.escape(p["title"]),
            description=html.escape(p["description"]),
            cdn=CDN,
            header=sub_static(header_tpl, slug),
            body=sub_static(body, slug),
            footer=sub_static(footer_tpl, slug),
        )
        out = os.path.join(DOCS, "index.html" if slug == "index" else f"{slug}.html")
        open(out, "w", encoding="utf-8").write(page_html)
        print(f"static  -> {os.path.relpath(out, ROOT)}")


WP_TEMPLATE = """<?php
/**
 * {template_comment}
 *
 * Generated from src/partials/{slug}.html by build.py — edit the partial,
 * not this file, then re-run `python3 build.py`.
 *
 * @package Cloudstaff
 */

get_header();
?>
<main class="site-main" id="main-content">
{body}
</main>
<?php
get_footer();
"""


def build_wp():
    os.makedirs(THEME, exist_ok=True)
    for slug, p in pages.items():
        body = sub_wp(read(SRC, "partials", f"{slug}.html"))
        tpl_name = p["wp_template"]
        comment = ("The front page template." if tpl_name == "front-page"
                   else f"Template Name: {p['nav_label']}\n * Template Post Type: page")
        out = os.path.join(THEME, f"{tpl_name}.php")
        open(out, "w", encoding="utf-8").write(
            WP_TEMPLATE.format(template_comment=comment, slug=slug, body=body))
        print(f"wp      -> {os.path.relpath(out, ROOT)}")
    # header.php / footer.php from the shared templates
    wp_header = """<?php
/**
 * Site header — generated from src/header.html by build.py.
 *
 * @package Cloudstaff
 */
?><!doctype html>
<html <?php language_attributes(); ?> data-theme="light">
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
""" + sub_wp(header_tpl)
    open(os.path.join(THEME, "header.php"), "w", encoding="utf-8").write(wp_header)
    wp_footer = sub_wp(footer_tpl) + """
<?php wp_footer(); ?>
</body>
</html>
"""
    open(os.path.join(THEME, "footer.php"), "w", encoding="utf-8").write(wp_footer)
    # copy custom css into theme
    shutil.copyfile(os.path.join(SRC, "site.css"), os.path.join(THEME, "site.css"))
    shutil.copyfile(os.path.join(SRC, "teambuilder.js"), os.path.join(THEME, "teambuilder.js"))
    shutil.copyfile(os.path.join(SRC, "coverage.js"), os.path.join(THEME, "coverage.js"))
    shutil.copyfile(os.path.join(SRC, "coworkers.js"), os.path.join(THEME, "coworkers.js"))
    shutil.copyfile(os.path.join(SRC, "cloudstaff-logo.png"), os.path.join(THEME, "cloudstaff-logo.png"))
    shutil.copyfile(os.path.join(SRC, "cloudstaff-logo-light.png"), os.path.join(THEME, "cloudstaff-logo-light.png"))
    for img in IMAGES:
        shutil.copyfile(os.path.join(SRC, img), os.path.join(THEME, img))
    # slug -> meta description map used by functions.php
    descriptions = {slug: p["description"] for slug, p in pages.items()}
    with open(os.path.join(THEME, "page-meta.json"), "w", encoding="utf-8") as f:
        json.dump(descriptions, f, indent=2)
    print("wp      -> header.php, footer.php, site.css, page-meta.json")


if __name__ == "__main__":
    build_static()
    build_wp()
    print("Done.")
