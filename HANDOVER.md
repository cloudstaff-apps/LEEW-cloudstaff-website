# Cloudstaff.com rebuild, handover

_Last updated: 2026-11-12._

## Summary

A 36-page static marketing site (23 core pages plus 13 customer success story pages) for Cloudstaff, built from shared partials and
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

## Start here next session (state at close, 2026-11-10 evening)

**Everything is committed, pushed and deployed. Nothing is in progress.** The
working tree was clean at close. Lee will pick this up in a new chat.

First steps for a new session:

1. Read this file end to end. It is the single source of truth.
2. Work on Lee's linked computer, not the cloud workspace (see "Ops notes").
   Clone `cloudstaff-apps/LEEW-cloudstaff-website` to a scratch folder outside
   the connected folders (last session used `~/work/site`, remote named `org`;
   it may still be there, in which case `git pull` it and check it is clean).
3. Read the token from `Documents\claude\cloudstaff-apps-push.txt`. Never commit it.
4. After any change: `python3 build.py && python3 tools/noindex.py`, commit, push
   `main`, wait for the Pages build to report the new sha, then check the live
   page in Chrome with `?v=<sha>` on the URL.
5. Update this file in the same commit when a rule, source or decision changes,
   and copy it to the project doc `claude/website-rebuild-status.md`.

Standing rules Lee has set (do not break these):

- Test site only. Every page in `docs/` stays noindexed.
- No em dashes anywhere. US spelling.
- No coloured accent edge on a box, and diagrams in the site palette only
  (see "House design rule").
- Copy should be punchy. Flag any fact or claim Claude wrote so Lee can confirm it.
- Never use "AI Toolkit" or "AI Toolbox". The platform is **Cloudstaff Q**.
- Do not claim 100% training compliance.
- The four removed Coworkers stay out (see "Excluded from the public directory").
- Material from the internal AI Coworker presentation stays off the site:
  pricing, cost comparisons, 10x claims, "over 100 Coworkers", competitor names.

What changed on 2026-11-10 (latest first):

- AI Coworkers: the process diagram and the "friction around the edges" circle
  diagram were redrawn in the site palette; the process diagram was cut from 14
  moving parts to 11 and from 31 connectors to 18.
- Site-wide: every single-side coloured edge on a callout, card, table column or
  blockquote was removed and replaced with a tinted fill and thin border.
- AI Training: new page. Hero "AI skills increase your value. They do not
  decrease it."; band headed "We're making AI your Cloudstaffer's superpower"
  with Lee's caped Cloudstaffer photo; five levels (1 to 3 included, 4 and 5
  advanced and client-paid); wording softened to "the standard we set for every
  Cloudstaffer".
- Cloudstaff Q: rewritten around Secure, Govern, Scale, No lock-in, with the
  concentric rings as the central image. AI Toolkit page merged into it.
- AI Consultancy: new page.
- AI Coworkers: hotspot screenshots, avatars, merged chatbot/comparison section
  with the three reach bars, circle diagram, section reorder.
- Customer Success Stories: Americas first, 13 internal story pages with photo
  heroes, nav label renamed.
- Typography: headings and paragraphs no longer wrap early, on all pages.
- Hosting: moved to the org repo; old personal repo deleted.

Questions raised with Lee and still unanswered (take no action until he replies):

- Arrivia and Metro Property Management appear as named videos while their
  written stories are anonymised. Keep both, or align them?
- Nine video-only customer cards have no written story behind them.
- The comparison scorecard notes for chat tools and agents, and the eleven
  "moving parts" labels in the process diagram, were written by Claude.
- "Human manager" wording remains in five places on AI Coworkers (the hero now
  says "a Cloudstaffer it reports to"). Change the rest to match?
- Hotspot 2 placement on the Coworker profile screenshot.
- AI Consultancy: "working direct with your Coworkers" was read as the client's
  staff (job functions and SOPs). Confirm.
- AI Training: Levels 4 and 5 share one card. Split them? Are Coffee Hour and
  the Survival Guide right for this page?
- The "Louis Reid" avatar looks female.
- Cloudstaff Q "see your IP and take it with you": is that backed by the contract?
- Brochure statistics on the AI pages were not independently re-verified.

## Public holiday planner (added 2026-11-12, draft, NOT in the menu)

- Page `public-holidays.html` (partial `src/partials/public-holidays.html`, logic
  `src/holidays.js`, styles `.hol-*` in `site.css`). Lee wants to refine it before
  it goes in the navigation, so nothing links to it. Do not add it to
  `header.html` or `footer.html` until he says so.
- Styled after the coverage tool. The client picks: which holidays the team takes
  off (theirs or the client's), the service country (Philippines, India, Colombia,
  Kenya), their own country (USA, Australia, New Zealand, UK) and a state, region
  or nation.
- "Take my public holidays off" pairs each weekday local holiday with a weekday
  client holiday. The pairing keeps both columns in date order and minimises the
  total gap in days; a holiday on the same date in both places is shown as "no
  swap needed". Holidays left over on either side are shown unpaired with a note
  to agree treatment with the Account Manager, because Cloudstaff's policy for
  those days has not been given. "Take their local holidays off" is a plain
  date-ordered list. Weekend holidays are listed separately underneath.
- **Data is held in the page**, in the JSON block `#hol-data` (Lee's instruction;
  it may move to a database later). 2027 only. `"t": 1` marks a date that is not
  final. Planner version is the `version` field (currently 1.1); bump it on change.
- **Sources.** publicholidays.info was Lee's suggested source but its 2026 pages
  had errors (Juneteenth missing from the USA, Black Saturday on a Sunday), so the
  data was taken from primary sources instead: Philippines Proclamation No. 1427;
  India DoPT memorandum of 16 July 2026 (the 17 gazetted holidays for Delhi
  offices, used as the national proxy); Colombia computed from Ley 51 of 1983;
  Kenya Public Holidays Act; USA OPM federal schedule; Australia Fair Work
  Ombudsman 2027 list; UK GOV.UK; New Zealand computed from the Holidays Act rules
  because Employment New Zealand had not published 2027.
- **USA states (v1.1, 2026-11-12):** the State list holds "Federal holidays only"
  plus all 50 states and DC. Each state adds its state government holidays to the
  federal list. These were computed from the statutory rules Claude knows, not
  checked against each state's published 2027 calendar, so treat them as moderate
  confidence. Federal holidays a state does not observe (Columbus Day in several
  states) are not removed. Election-day holidays are included only where the state
  observes one every year (New Jersey, New York, Virginia, Indiana).
- **Known gaps to raise with Lee:**
  Philippine Eid'l Fitr and Eid'l Adha are estimates until proclaimed; Indian
  holidays vary by state; Kenya's 2027 election day is not included; Tasmanian
  regional days, part-day holidays (Christmas Eve and New Year's Eve evenings) and
  Philippine city holidays are left out; the Victorian AFL Grand Final Friday is an
  estimate.

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

## House design rule (important)

**No coloured accent edge on a box.** Lee reads a text box with one coloured
side (a thick left or top border) as a sign of AI-generated content. Highlight a
callout with a tinted background and a thin border all round, never a single
coloured edge. This includes blockquotes.

**Diagrams use the site palette only.** Brand blue, navy text, white and pale
grey boxes. No pastel multi-colour fills and no black connector lines: Lee found
those out of character and less professional. Keep diagrams sparse. The process
diagram on AI Coworkers is generated by `tools/gen_process_art.py --write`
(eleven moving parts, eighteen connectors).

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

## Pages (35: 22 core plus 13 story pages)

Home, What Is Remote Staffing, How It Works, Time Zones, Pricing, Team Builder,
Roles, Security, Why Cloudstaff, Customers, **AI Enabled Staff + AI Coworkers +
Cloudstaff Q**, International hub + 4 center pages (Philippines/Colombia/India/Kenya),
CFO Guide, Contact.

## What shipped this session

- **Customer Success Stories** (`customers.html`, nav label "Customer Success
  Stories"): 22 client cards ordered by region, Americas first, then Asia Pacific,
  then the stats band, then written-only stories. 17 carry video: 6 on Vimeo,
  Avetta and Alliance on YouTube, and 9 short YouTube testimonial clips that have
  name and industry only because no written story exists for them (Riverton
  Insurance, Thrive Causemetics, Arrivia, J4RVIS, Fitness Passport, RISE Initiative
  Australia, PropTech Guru, Nexgen Australia, Metro Property Management).
  The 6 Vimeo videos are the same films as Cloudstaff's YouTube uploads, so do
  not add the YouTube versions as well.
- **Story pages** (`story-*.html`, 13 of them): generated by
  `tools/gen_stories.py` from `tools/stories.json`. Each entry combines two
  sources. The headline, four stat tiles, situation, challenge, solution and
  facts come from the 12 Cloudstaff success story PDFs Lee supplied on
  2026-11-10. The `web` block (about paragraph, company size, challenge and
  solution intros, growth timeline, results section, "Built to last" closing,
  fuller quote, and image paths) was carried over from the matching
  cloudstaff.com/success-stories page the same day. Wipfli has no PDF, so its
  page is built entirely from its cloudstaff.com page. To change a story, edit
  `stories.json`, run `python3 tools/gen_stories.py`, then build. Do not
  hand-edit `src/partials/story-*.html`. Every "Read the full story" link on the
  Customers page points to these internal pages; nothing links to
  cloudstaff.com/success-stories. Anonymised stories stay anonymised.
- **Story images** (team photo in the hero, client logo, speaker portrait) load
  from `www.cloudstaff.com/wp-content/uploads/`. They are not in the repo. The
  speaker portraits also replace the initials avatars on the Customers cards.
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

## AI section sources (added 2026-11-10)

- **Naming: "AI Toolkit" is the old name for Cloudstaff Q.** Never use "AI
  Toolkit" or "AI Toolbox" on the site. The separate AI Toolkit page created on
  2026-11-10 was merged into `cloudstaff-q.html` the same day and deleted.
- **Cloudstaff Q messaging (Lee, 2026-11-10):** "AI needs to be secure. Cloudstaff
  Q is our platform that helps you adopt AI securely, govern it confidently and
  scale your AI usage responsibly." The page runs in that order: Security, then
  Governance, then Scalability, then No lock-in. Framing: nobody knows what AI
  looks like in one, five or ten years, but it will disrupt every business and
  every employee, so you need a platform that is safe today. No lock-in means the
  client can see their IP and take it with them if they leave ("not that we want
  you to leave"). Keep the tone punchy.
- **Cloudstaff Q page** is built around the four concentric "rings of protection"
  (Staging, Private production, Limited production, Public production), drawn as
  an interactive inline SVG after the All Apps diagram in the public brochure
  "Cloudstaff AI Toolbox" (V260624). It also holds Govern (AI Policy Builder,
  Badge Pack AI, AI Access Controls), private AI platforms (AllChat, AllBot, AI
  Voice Support), and AI Security Testing, which is an **add-on service**, not
  part of Q itself.
- **AI Training structure (Lee, 2026-11-10):** every Cloudstaffer is AI-trained,
  because "AI skills increase your value. They do not decrease it." Cloudstaff
  Academy trainers roll it out to all 8,000 Cloudstaffers. Level 1: AI
  fundamentals, safety and security (must come first). Level 2: good prompt
  writing, to get the answer needed while minimising rework and hallucinations.
  Level 3: writing their own agents so parts of the role can be automated under
  their supervision. Levels 1 to 3 are table stakes and Cloudstaff covers the
  cost. Levels 4 and 5 are advanced, voluntary, customised to a client's
  industry, a job role, or the client's specific needs (example: an advanced
  course for accountants), and clients pay for them. Lee did not say how Level 4
  differs from Level 5, so the page presents them together.
- Do not claim 100% training compliance. Say the first three levels are "the
  standard we set for every Cloudstaffer", not that every Cloudstaffer takes them.
- AI Training headline: "We're making AI your Cloudstaffer's superpower". The
  caped Cloudstaffer beside it is Lee's own image (`src/ai-superpower.webp`). His
  file was a JPG with a checkerboard baked in, so the background was cut out
  before use. It sits on a CSS sunburst (`.superpower` in `site.css`).
- **AI Training** (`ai-training.html`) and **AI Consultancy**
  (`ai-consultancy.html`) are their own pages and are NOT part of Cloudstaff Q.
  AI Coffee Hour and the AI Survival Guide sit on the Training page. Consultancy
  positioning from Lee: consultants on the ground in the USA and Australia build
  fully customised AI Coworkers, and specialise in working directly with the
  client's staff, examining job functions and standard operating procedures.
- The brochure PDF's text layer is corrupt, so it was read by OCR. Third-party
  statistics are quoted with the brochure's attributions (McKinsey, IBM,
  Microsoft and LinkedIn, PwC). Its Cisco and BCG statistics were left out.
- **AI Coworkers additions** ("One of the team", the invoice process example, the
  comparison cards, "Where do you start?", the six onboarding steps, and "The
  people behind every Coworker") come from an internal Cloudstaff AI Coworker
  presentation. It was internal, so these were deliberately NOT carried over and
  should not be added without Lee's say-so: all pricing and setup costs, the cost
  comparisons for Tracy, Nicola and Mike, the "10x faster, 10x cheaper, better
  than a human" claims, the "over 100 Coworkers" library figure, competitor
  product names, and the strategy and next-steps slides.
- **"Why a chatbot is not enough" and "How is a Cloudstaff AI Coworker
  different?" are one section** (`#how-it-compares`). The process diagram (drawn
  by `tools/gen_process_art.py`, three tier groups `pa-t1` to `pa-t3`) sits beside
  three vertical bars whose heights show how far down the stack each option
  reaches: chat tools reach the request, AI agents reach the six steps ("the hub
  data"), the AI Coworker reaches the whole stack. Hovering or selecting a bar
  dims the tiers that option cannot reach, swaps a one-line caption, and swaps
  the seven-point scorecard underneath. The Coworker is selected by default.
  Lee's framing: a chatbot gets you the chat, an agent gets you to the hub data
  set, the AI Coworker traverses the entire stack end to end. The Coworker column
  and four points against the others come from the presentation; the remaining
  scorecard notes on chat tools and agents were written by Claude.
- The "core competency" circle diagram in "Where do you start?" is hand-placed
  inline SVG in the partial, based on Lee's slide.
- Section order on AI Coworkers: What is an AI Coworker, One of the team, Nine
  things, Meet the Coworkers, the directory, Why a chatbot is not enough (with
  the comparison), Where do you start, The people behind every Coworker,
  Responsible by default.
- **"One of the team" hotspots** (AI Coworkers page): two screenshots with numbered
  hotspots that open on hover, focus or tap, pure CSS. `src/coworker-profile.png`
  is the ExpenseBoss profile of Chris Hayes with the app URLs and part of his
  manager's email address masked, as Lee masked them. `src/coworker-team.png` is
  the Cloudstaff Q Team view cropped to its first row of cards, because the
  second row shows Taskboss, which is on the excluded list. Images in `src/` are
  copied by the `IMAGES` list in `build.py`. On phones the popups are replaced by
  a numbered list under the images.
- Cloudstaff Q tiles were enriched from the same presentation (hosting options,
  hundreds of models, logging of communications and decisions).

## "AI-enabled Cloudstaffers" wording

Reviewed all 13 uses of "Cloudstaffer(s)" on 2026-11-10. Three now read
"AI-enabled Cloudstaffer(s)" and link to the AI Enabled Staff page (Home and
Pricing savings sentences, Why Cloudstaff infrastructure intro). The other ten
stay plain on purpose: headcount stats, client success stories, the productivity
ladder on Roles, the definition on AI Enabled Staff itself, and the data-access
card on Security. Inline links in body copy use `class="text-link"` (`src/site.css`).

## Excluded from the public directory

Removed on 2026-11-10 at Lee's instruction as not for website consumption. Do not
re-add: TheBoss (Dylan Owen), Bruceboss (Thomas Jackson), Taskboss (Luke Riley),
Try Yoga (Sadie Clarke).

## Open follow-ups

- **Coworker directory avatars:** done 2026-11-10. The 41 named Coworkers use
  portraits from Lee's "AI Avatars" folder, resized to 176px in `src/avatars/`
  and named after the Coworker (`emma-frost.jpg`). `coworkers.js` builds the path
  from the name and falls back to initials if a file is missing. Three source
  files were spelled differently from the directory and were matched by hand:
  "Helen Forster" (Helen Foster), "Jane Doyne" (Jane Doyle) and "Melissa Neilson"
  (Melissa Nelson). The three "In development" entries have no person and keep
  their initials badge.
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
