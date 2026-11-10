# Cloudstaff.com rebuild, handover

_Last updated: 2026-11-10._

## Summary

A 20-page static marketing site for Cloudstaff, built from shared partials and
deployed to GitHub Pages. It repurposes the CFO Kit, the live cloudstaff.com
success stories, and cloudstaff.ai, optimised for a US audience and positioned
as the market leader. Everything is token-driven on top of the Cloudstaff
Design System, with an owned `src/site.css` scaffolding layer.

- **Live:** https://cloudstaff-apps.github.io/LEEW-cloudstaff-website/
- **Repo:** https://github.com/cloudstaff-apps/LEEW-cloudstaff-website (Pages source `main` / `/docs`).
  This is the **only** repo for this site. It sits in the corporate GitHub org.
- There is no other copy. Lee's old personal repo (`LEEW-CS/cloudstaff-website`, served at
  `leew-cs.github.io/cloudstaff-website`) was deleted on 2026-11-10 after its history was
  copied here. If either name turns up in old notes or chats, ignore it.

## Prototype is noindexed (important)

Every page in `docs/` carries
`<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">`.
It is injected by `tools/noindex.py`, a post-build step, so **always build with**:

    python3 build.py && python3 tools/noindex.py

Running `build.py` alone strips the tag and makes the prototype indexable again.
`python3 tools/noindex.py --check` verifies without writing (exit 1 on any problem).
`--dry-run` reports what would change. The script also fails if any noindex directive
leaks into `wordpress/cloudstaff-theme/`, which must stay indexable for the live site.
`robots.txt` is not used: the site publishes to a subpath, and crawlers only read
robots.txt at the host root.

## House writing rule (important)

**No em dashes anywhere.** Lee considers them an AI tell. Use full stops and
fresh sentences, commas, colons, or parentheses instead. En dashes in numeric
or time ranges (9am–5pm, 2.5–3) are fine. This applies to every partial, JS
string, meta description, and CSS comment. If you add content, do not introduce
`&mdash;`, `—`, or `—`.

## Architecture / build

- Author in `src/` partials. `python3 build.py && python3 tools/noindex.py` renders:
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
    coworker collage from cloudstaff.ai), and a **filterable directory** of 44
    Coworkers (41 live, 3 in development) across 13 functions (`coworkers.js`) with a search box.
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

- **Token:** a fine-grained PAT owned by `cloudstaff-apps` is saved on Lee's computer
  at `Documents\claude\cloudstaff-apps-push.txt` (expires 2027-02-08). Read it from
  there each session. Never commit it or write it into a stored remote URL. A new
  token for this org must have Resource owner set to `cloudstaff-apps` and may need
  an org owner to approve it before it works.
- **Where to run git:** on Lee's linked computer (its shell has git, python3 and
  network access to github.com). Clone to a scratch folder outside the connected
  folders, pass the token through an inline credential helper, and push `main`.
  The cloud workspace's proxy refuses the `cloudstaff-apps` repo, so it cannot deploy.
- **Commit identity:** committer `Claude <noreply@anthropic.com>`.
- **Verify a deploy** with the GitHub API
  (`GET /repos/cloudstaff-apps/LEEW-cloudstaff-website/pages/builds/latest` should
  report `status: built` and the pushed commit sha), then load the live site in the
  browser pane and check the pages. `github.io` is blocked for curl from both the
  cloud workspace and the linked computer's shell.
- **Deploy lag + CDN cache:** Pages can take a couple of minutes; the bare live
  URL is edge-cached ~10 min, so append `?v=` to bust while verifying, and tell
  Lee to hard-refresh pages he had already opened.
- The cloud workspace is wiped between sessions. Nothing saved there survives, so
  re-clone each session using the token file above.

## Excluded from the public directory

Removed on 2026-11-10 at Lee's instruction as not for website consumption. Do not
re-add: TheBoss (Dylan Owen), Bruceboss (Thomas Jackson), Taskboss (Luke Riley),
Try Yoga (Sadie Clarke).

## Open follow-ups

- **Coworker directory avatars:** the 44 directory cards use initials avatars
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
