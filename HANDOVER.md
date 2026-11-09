# Cloudstaff.com rebuild, handover

_Last updated: 2026-11-09 (end of session)._

## Summary

A 20-page static marketing site for Cloudstaff, built from shared partials and
deployed to GitHub Pages. It repurposes the CFO Kit, the live cloudstaff.com
success stories, and cloudstaff.ai, optimised for a US audience and positioned
as the market leader. Everything is token-driven on top of the Cloudstaff
Design System, with an owned `src/site.css` scaffolding layer.

- **Live:** https://leew-cs.github.io/cloudstaff-website/
- **Repo:** https://github.com/LEEW-CS/cloudstaff-website (public; Pages source `main` / `/docs`)

## House writing rule (important)

**No em dashes anywhere.** Lee considers them an AI tell. Use full stops and
fresh sentences, commas, colons, or parentheses instead. En dashes in numeric
or time ranges (9am–5pm, 2.5–3) are fine. This applies to every partial, JS
string, meta description, and CSS comment. If you add content, do not introduce
`&mdash;`, `—`, or `—`.

## Architecture / build

- Author in `src/` partials. `python3 build.py` renders:
  - `docs/` (the static site GitHub Pages serves), and
  - `wordpress/cloudstaff-theme/` (a parallel WP theme, not activated).
- Shared chrome: `src/header.html`, `src/footer.html`. Page bodies:
  `src/partials/<slug>.html`. Page list + titles/descriptions: `src/meta.json`.
- Placeholders resolved at build: `{{URL:slug}}`, `{{ACTIVE:slug}}`,
  `{{ASSET:file}}`, `{{ART:x}}`, `{{SEAL:x}}`, `{{LOGO}}` / `{{LOGO:light}}`,
  `{{FLAG:xx}}`.
- Icons: `<i class="fa-light fa-NAME">` must be mapped in `FA_MAP` in
  `tools/icons.py`, or the build raises `KeyError`. Icons are inline SVG glyphs.
- The four center pages are generated: edit the `COUNTRIES` / `OTHER_LINKS`
  dicts in `tools/gen_centers.py`, run `python3 tools/gen_centers.py`, then
  `python3 build.py`. Do not hand-edit `src/partials/center-*.html` (regenerated).
- Interactive widgets are plain JS copied into `assets/` by build.py:
  `teambuilder.js`, `coverage.js`, `coworkers.js`.

## Navigation

Top level: **About ▾** · **AI Enabled Staff ▾** · **Roles & Industries ▾** ·
International · CFO Guide · Contact Us, plus quiet "Jobs" and "Talk to an Expert".
- About ▾: What Is Remote Staffing?, How It Works, Time Zones, Why Cloudstaff, Security, Customers
- AI Enabled Staff ▾: Overview, AI Coworkers, Cloudstaff Q
- Roles & Industries ▾: All roles, Team Builder, Pricing & Savings

## Pages (20)

Home, What Is Remote Staffing, How It Works, Time Zones, Pricing, Team Builder,
Roles, Security, Why Cloudstaff, Customers, **AI Enabled Staff + AI Coworkers +
Cloudstaff Q**, International hub + 4 center pages (Philippines/Colombia/India/Kenya),
CFO Guide, Contact.

## What shipped this session

- **Customers page** (`customers.html`): 13 success stories, 6 with embedded
  Vimeo videos, 7 written, from cloudstaff.com/success-stories.
- **International**: interactive "Follow the sun" coverage tool (`coverage.js`)
  with day/night shift bars (sun/moon SVG). Center "Explore" links are buttons;
  Specialist-hubs card has a Contact-us button; sibling-country pills carry flags.
- **Time Zones page** (`timezones.html`): a standalone copy of the coverage tool.
- **AI Enabled Staff** section (built from board slides + cloudstaff.ai, with
  the internal "provisional / for-validation" framing deliberately excluded):
  - Overview: "More capacity. Same control.", two layers (AI Coworkers +
    Cloudstaff Q), three pillars with "Evidence today" proof lines, and the two
    engagement models (AI-enabled staffing / Human + AI solutions).
  - AI Coworkers: nine traits, featured Mike/Tracy/Nicola (real photos +
    coworker collage from cloudstaff.ai), and a **filterable directory** of 48
    live Coworkers across 13 functions (`coworkers.js`) with a search box.
  - Cloudstaff Q: the secure platform / control layer.
- **Logo**: official Cloudstaff lockup image in the header; official reverse
  (all-white) lockup in the dark footer. `src/cloudstaff-logo*.png`.
- **Flags everywhere**: real flag images via `{{FLAG:xx}}` -> flagcdn.com
  (OS flag emoji rendered as "PH/CO/IN/KE" letters on Windows). Used on the
  International center cards, hub/office badges and sibling pills, Customers
  delivery tile, roles capability hubs, and Contact offices + phone grid.
- **Contact page**: real office addresses + a phone grid by country (flags, tel
  links) + social links, from cloudstaff.com/contact.
- **Em dashes removed site-wide** (261 in content), with comma splices repaired
  into full sentences and a clobbered Security comparison table restored.

## Ops notes / gotchas

- **Push:** a fine-grained PAT is at `/home/claude/.gh_pat` (session-local;
  gone when the container is reclaimed). Push via an authed URL with proxy env
  unset: `export -n HTTP_PROXY HTTPS_PROXY http_proxy https_proxy` then
  `git push "https://x-access-token:$TOKEN@github.com/leew-cs/cloudstaff-website.git" HEAD:main`.
  After each push run `git update-ref refs/remotes/origin/main HEAD` so the stop
  hook does not report a false "unpushed".
- **Commit identity:** the stop hook requires committer `Claude
  <noreply@anthropic.com>`. Run `git config user.email noreply@anthropic.com &&
  git config user.name Claude` before committing.
- **Proxy blocks curl to leew-cs.github.io (403)**, so you cannot verify live
  pages with curl from the container. Use the Chrome browser tools, or check the
  build API: `GET /repos/leew-cs/cloudstaff-website/pages/builds/latest` returns
  `status: built` + the commit sha.
- **Deploy lag + CDN cache:** Pages can take a couple of minutes; the bare live
  URL is edge-cached ~10 min, so append `?v=` to bust while verifying, and tell
  Lee to hard-refresh pages he had already opened.
- Container is ephemeral. Recovery after a reclaim: re-clone from GitHub with a
  fresh PAT (no local state survives).

## Open follow-ups

- **Coworker directory avatars:** the 48 directory cards use initials avatars
  (EF, HF, ...). Only Mike/Tracy/Nicola have public photos (used on the featured
  cards). To use real portraits, Lee needs to export the avatar images from the
  internal Coworker app (or give URLs/a folder), then swap `.avatar-initials`
  for `<img>` in `coworkers.js`.
- **AI content to confirm for public use:** the Mike "~6,000 tickets / ~600
  reworks" stat and the named example Coworkers; whether to name **HaloMD** (a
  client) under the second pillar's evidence, which is currently generalised to
  "in-production client workflows"; the **Other** category descriptions were
  inferred from unit names (source had none), so verify; **Legal & compliance**
  entries are marked "In development".
- **Team Builder** pricing is all placeholder. Needs real rate cards + JDs, and
  the "Get my real quote" / contact form wired to a CRM backend.
- Replace Unsplash heroes, initial-avatar testimonials and interpreted cert
  seals with real brand assets; verify Philippines/India center copy (their
  source pages were WAF-blocked).
- Verify the **India phone number** on Contact (displayed vs tel-link differed
  on the source).
- Flags and the AI imagery load from external hosts (flagcdn.com, cloudstaff.ai)
  at view time. Mirror into the repo if a fully self-hosted site is wanted.
- WP theme is generated but not activated; activation steps still to document.
- Lee can revoke the PAT when finished.
