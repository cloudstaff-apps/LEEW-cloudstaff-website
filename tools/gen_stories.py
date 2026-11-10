#!/usr/bin/env python3
"""Generator for the Customer Success Story pages.

Reads tools/stories.json (one entry per client: headline, stats, situation,
challenge, solution and facts transcribed from the Cloudstaff success story PDFs,
plus a "web" block carried over from the matching cloudstaff.com/success-stories
page: about, intros, growth, results, closing section and image paths) and
writes src/partials/story-<name>.html, then makes sure each page is listed in
src/meta.json. Run it, then build:

    python3 tools/gen_stories.py && python3 build.py && python3 tools/noindex.py

Do not hand-edit src/partials/story-*.html (regenerated). Edit stories.json.
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTIALS = os.path.join(ROOT, "src", "partials")
META = os.path.join(ROOT, "src", "meta.json")
STORIES = json.load(open(os.path.join(ROOT, "tools", "stories.json"), encoding="utf-8"))
IMG = "https://www.cloudstaff.com/wp-content/uploads/"

FACT_LABELS = [("INDUSTRY", "Industry"), ("HEADQUARTERS", "Headquarters"), ("LOCATION", "Location"),
               ("PARTNERSINCE", "Partner since"), ("DELIVERYCENTER", "Delivery center"),
               ("DELIVERYCENTERS", "Delivery centers")]


def e(s):
    return html.escape(s, quote=False).replace("→", " &rarr; ").replace("•", "&middot;")


def initials(who):
    if who.isupper() or "," in who:
        return e(who.split(",")[0][:2].upper())
    return e("".join(p[0] for p in who.split()[:2]).upper())


def video(s):
    kind, vid = s["video"]
    src = ("https://player.vimeo.com/video/" + vid) if kind == "vimeo" else ("https://www.youtube-nocookie.com/embed/" + vid)
    return ('<div class="cs-video"><iframe src="%s" title="%s, Cloudstaff customer success story" loading="lazy" '
            'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen; web-share" '
            'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>' % (src, e(s["name"])))


def check(item):
    m = re.match(r"^([^.]{3,40})\. (.+)$", item)
    if m and len(m.group(1).split()) <= 5:
        return "<li><strong>%s.</strong> %s</li>" % (e(m.group(1)), e(m.group(2)))
    return "<li>%s</li>" % e(item)


def step(g):
    m = re.match(r"^([^:]{3,24}): (.+)$", g)
    if m:
        return '      <li><span class="cs-tag">%s</span><span>%s</span></li>' % (e(m.group(1)), e(m.group(2)))
    return '      <li><span class="story-dot" aria-hidden="true"></span><span>%s</span></li>' % e(g)


def band(cls, inner):
    return '<section class="%s">\n  <div class="site-band-inner">\n%s\n  </div>\n</section>\n' % (cls, inner)


def page(s):
    f = s["facts"]
    w = s.get("web", {})
    named = bool(w.get("logo"))
    industry = e(f.get("INDUSTRY", ""))
    out = []

    # hero: the team photo is the background image
    # photo_focus_y: vertical position (percent) of the people in the photo, so the
    # short, wide hero band crops to them and not to ceilings, sky or floor.
    style = (' style="--hero-image: url(\'%s%s\'); --hero-focus: %d%%"' % (IMG, w["photo"], w.get("photo_focus_y", 35))) if w.get("photo") else ""
    out.append(
        '<section class="site-hero site-hero-photo center-hero story-hero"%s>\n'
        '  <div class="site-band-inner">\n'
        '    <div class="site-hero-copy">\n'
        '    <span class="eyebrow"><a href="{{URL:customers}}" class="center-back">Customer Success Stories</a> &rarr; %s</span>\n'
        '    <h1>%s</h1>\n'
        '    <p>%s</p>\n'
        '    <a href="{{URL:contact}}" class="button button-lg">Talk to an expert</a>\n'
        '    </div>\n  </div>\n</section>\n'
        % (style, industry, e(s["title"]), " &middot; ".join(e(x) for x in s["meta"])))

    # numbers + voice
    tiles = "\n".join(
        '      <div class="stat-tile"><div class="stat-tile-label">%s</div><div class="stat-tile-value">%s</div></div>' % (e(l), e(v))
        for v, l in s["stats"])
    quote = w.get("quote") or s.get("quote")
    if quote:
        if w.get("portrait"):
            avatar = '<img class="avatar-photo" src="%s%s" alt="" loading="lazy">' % (IMG, w["portrait"])
        else:
            avatar = '<span class="avatar-initials">%s</span>' % initials(s["who"])
        role = (", " + e(s["role"])) if s.get("role") else ""
        voice = ('    <figure class="card cs-story story-quote">\n'
                 '      <blockquote>&ldquo;%s&rdquo;</blockquote>\n'
                 '      <figcaption>%s<span><strong>%s</strong>%s</span></figcaption>\n'
                 '    </figure>' % (e(quote), avatar, e(s["who"]), role))
    else:
        p = s["pull"]
        voice = ('    <div class="card cs-story story-quote">\n      <h3>%s</h3>\n      <p>%s</p>\n      <p><small>%s</small></p>\n    </div>'
                 % (e(p["title"]), e(p["text"]), e(p["sub"])))
    out.append(band("site-band",
                    '    <span class="eyebrow">At a glance</span>\n    <h2>The partnership in numbers</h2>\n'
                    '    <div class="grid-4 center-glance">\n%s\n    </div>\n%s' % (tiles, voice)))

    # about + situation, with video and facts
    rows = [(lab, f[k]) for k, lab in FACT_LABELS if f.get(k)]
    if w.get("size"):
        rows.insert(1, ("Company size", w["size"]))
    facts = "\n".join("          <div><dt>%s</dt><dd>%s</dd></div>" % (lab, e(v)) for lab, v in rows)
    logo = ('          <img class="story-logo" src="%s%s" alt="%s logo" loading="lazy">\n' % (IMG, w["logo"], e(s["name"]))) if named else ""
    vis = ("        " + video(s) + "\n") if s.get("video") else ""
    about = ("      <p>%s</p>\n      <h3>The situation</h3>\n" % e(w["about"])) if w.get("about") else ""
    sit = "\n".join("      <p>%s</p>" % e(x) for x in s["situation"])
    about_h2 = e(("About " + s["name"]) if named else "About the client")
    out.append(
        '<section class="site-band site-band-tinted">\n  <div class="site-band-inner story-split">\n    <div>\n'
        '      <span class="eyebrow">%s</span>\n      <h2>%s</h2>\n%s%s\n    </div>\n'
        '    <div class="site-visual">\n      <div class="stack-lg">\n%s        <dl class="card story-facts">\n%s%s\n        </dl>\n'
        '      </div>\n    </div>\n  </div>\n</section>\n' % (industry, about_h2, about, sit, vis, logo, facts))

    # challenge
    intro = ("    <p>%s</p>\n" % e(w["challenge_intro"])) if w.get("challenge_intro") else ""
    cards = "\n".join(
        '      <div class="card">\n        <div class="step-number">%d</div>\n        <h3>%s</h3>\n        <p>%s</p>\n      </div>'
        % (i + 1, e(h), e(t)) for i, (h, t) in enumerate(s["challenge"]))
    out.append(band("site-band",
                    '    <span class="eyebrow">Before Cloudstaff</span>\n    <h2>The challenge</h2>\n%s    <div class="grid-3">\n%s\n    </div>'
                    % (intro, cards)))

    # solution
    intro = ("    <p>%s</p>\n" % e(w["solution_intro"])) if w.get("solution_intro") else ""
    items = "\n".join("      " + check(x) for x in s["solution"])
    out.append(band("site-band site-band-tinted",
                    '    <span class="eyebrow">What Cloudstaff delivered</span>\n    <h2>The solution</h2>\n%s    <ul class="story-checks">\n%s\n    </ul>'
                    % (intro, items)))

    # growth
    growth = w.get("growth") or ["%s: %s" % (h, t) for h, t in s["timeline"]]
    out.append(band("site-band",
                    '    <span class="eyebrow">Over time</span>\n    <h2>Growth and evolution</h2>\n    <ol class="story-timeline">\n%s\n    </ol>'
                    % "\n".join(step(g) for g in growth)))

    # results
    if w.get("results"):
        cards = "\n".join(
            '      <div class="card story-result">\n        <h3>%s</h3>\n        <p>%s</p>\n      </div>'
            % (e(a.rstrip(",:")), e(b[:1].upper() + b[1:])) for a, b in w["results"])
        out.append(band("site-band site-band-tinted",
                        '    <span class="eyebrow">The outcome</span>\n    <h2>The results</h2>\n    <p>%s</p>\n    <div class="grid-3">\n%s\n    </div>'
                        % (e(w["results_intro"]), cards)))

    # closing
    closing = ""
    if w.get("closing"):
        closing = ('    <span class="eyebrow">Looking ahead</span>\n    <h2>Built to last</h2>\n%s\n'
                   % "\n".join("    <p>%s</p>" % e(x) for x in w["closing"]))
    out.append(band("site-band",
                    closing + '    <p><a href="{{URL:customers}}" class="button-link">&larr; All customer success stories</a></p>'))

    out.append('<section class="site-cta">\n  <div class="site-band-inner">\n    <h2>Ready to build your global team?</h2>\n'
               '    <p>Talk to us about embedding world-class remote talent in your firm.</p>\n'
               '    <a href="{{URL:contact}}" class="button button-inverse button-lg">Talk to an expert</a>\n  </div>\n</section>\n')
    return "\n".join(out)


def main():
    meta = json.load(open(META, encoding="utf-8"))
    pages = meta["pages"]
    by_slug = {p["slug"]: p for p in pages}
    at = next(i for i, p in enumerate(pages) if p["slug"] == "customers") + 1
    for s in STORIES:
        open(os.path.join(PARTIALS, s["slug"] + ".html"), "w", encoding="utf-8").write(page(s))
        entry = {
            "slug": s["slug"],
            "wp_template": "page-" + s["slug"],
            "nav_label": s["name"],
            "in_nav": False,
            "title": "%s: Customer Success Story | Cloudstaff" % s["name"],
            "description": s["situation"][-1],
        }
        if s["slug"] in by_slug:
            by_slug[s["slug"]].update(entry)
        else:
            pages.insert(at, entry)
            at += 1
        print("story   -> src/partials/%s.html" % s["slug"])
    with open(META, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


if __name__ == "__main__":
    main()
