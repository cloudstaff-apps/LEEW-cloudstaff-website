#!/usr/bin/env python3
"""Generator for the Customer Success Story pages.

Reads tools/stories.json (one entry per client, transcribed from the Cloudstaff
success story PDFs) and writes src/partials/story-<name>.html, then makes sure
each page is listed in src/meta.json. Run it, then build:

    python3 tools/gen_stories.py && python3 build.py && python3 tools/noindex.py

Do not hand-edit src/partials/story-*.html (regenerated). Edit stories.json.
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTIALS = os.path.join(ROOT, "src", "partials")
META = os.path.join(ROOT, "src", "meta.json")
STORIES = json.load(open(os.path.join(ROOT, "tools", "stories.json"), encoding="utf-8"))

FACT_LABELS = [("INDUSTRY", "Industry"), ("HEADQUARTERS", "Headquarters"), ("LOCATION", "Location"),
               ("PARTNERSINCE", "Partner since"), ("DELIVERYCENTER", "Delivery center"),
               ("DELIVERYCENTERS", "Delivery centers")]


def e(s):
    return html.escape(s, quote=False).replace("→", " &rarr; ").replace("•", "&middot;")


def initials(who):
    if who.isupper() or "," in who:
        return e(who.split(",")[0][:2].upper())
    parts = who.split()
    return e("".join(p[0] for p in parts[:2]).upper())


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


def page(s):
    f = s["facts"]
    industry = f.get("INDUSTRY", "")
    tiles = "\n".join(
        '      <div class="stat-tile"><div class="stat-tile-label">%s</div><div class="stat-tile-value">%s</div></div>' % (e(l), e(v))
        for v, l in s["stats"])
    if s.get("quote"):
        voice = '''    <figure class="card cs-story story-quote">
      <blockquote>&ldquo;%s&rdquo;</blockquote>
      <figcaption><span class="avatar-initials">%s</span><span><strong>%s</strong>%s</span></figcaption>
    </figure>''' % (e(s["quote"]), initials(s["who"]), e(s["who"]), (", " + e(s["role"])) if s.get("role") else "")
    else:
        p = s["pull"]
        voice = '''    <div class="card cs-story story-quote">
      <h3>%s</h3>
      <p>%s</p>
      <p><small>%s</small></p>
    </div>''' % (e(p["title"]), e(p["text"]), e(p["sub"]))
    facts = "\n".join("          <div><dt>%s</dt><dd>%s</dd></div>" % (lab, e(f[k])) for k, lab in FACT_LABELS if f.get(k))
    visual = ("        " + video(s) + "\n") if s.get("video") else ""
    sit = "\n".join("      <p>%s</p>" % e(x) for x in s["situation"])
    chal = "\n".join('''      <div class="card">
        <div class="step-number">%d</div>
        <h3>%s</h3>
        <p>%s</p>
      </div>''' % (i + 1, e(h), e(t)) for i, (h, t) in enumerate(s["challenge"]))
    sol = "\n".join("      " + check(x) for x in s["solution"])
    tl = "\n".join('''      <div class="card story-step">
        <span class="cs-tag">%s</span>
        <p>%s</p>
      </div>''' % (e(h), e(t)) for h, t in s["timeline"])
    return '''<section class="site-hero site-hero-photo center-hero">
  <div class="site-band-inner">
    <div class="site-hero-copy">
    <span class="eyebrow"><a href="{{URL:customers}}" class="center-back">Customer Success Stories</a> &rarr; %(industry)s</span>
    <h1>%(title)s</h1>
    <p>%(meta)s</p>
    <a href="{{URL:contact}}" class="button button-lg">Talk to an expert</a>
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <span class="eyebrow">The results</span>
    <h2>The partnership in numbers</h2>
    <div class="grid-4 center-glance">
%(tiles)s
    </div>
%(voice)s
  </div>
</section>

<section class="site-band site-band-tinted">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">%(industry)s</span>
      <h2>The situation</h2>
%(sit)s
    </div>
    <div class="site-visual">
      <div class="stack-lg">
%(visual)s        <dl class="card story-facts">
%(facts)s
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <span class="eyebrow">Before Cloudstaff</span>
    <h2>The challenge</h2>
    <div class="grid-3">
%(chal)s
    </div>
  </div>
</section>

<section class="site-band site-band-tinted">
  <div class="site-band-inner">
    <span class="eyebrow">What Cloudstaff delivered</span>
    <h2>The solution</h2>
    <ul class="story-checks">
%(sol)s
    </ul>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <span class="eyebrow">Over time</span>
    <h2>Growth and evolution</h2>
    <div class="grid-3">
%(tl)s
    </div>
    <p><a href="{{URL:customers}}" class="button-link">&larr; All customer success stories</a></p>
  </div>
</section>

<section class="site-cta">
  <div class="site-band-inner">
    <h2>Ready to build your global team?</h2>
    <p>Talk to us about embedding world-class remote talent in your firm.</p>
    <a href="{{URL:contact}}" class="button button-inverse button-lg">Talk to an expert</a>
  </div>
</section>
''' % dict(industry=e(industry), title=e(s["title"]), meta=" &middot; ".join(e(x) for x in s["meta"]),
           tiles=tiles, voice=voice, sit=sit, visual=visual, facts=facts, chal=chal, sol=sol, tl=tl)


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
