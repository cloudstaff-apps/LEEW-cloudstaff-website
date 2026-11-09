#!/usr/bin/env python3
"""One-off generator for the four International Services Center country pages.
Writes src/partials/<slug>.html. Run once; the output files are normal partials
that build.py consumes. Re-running regenerates them.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTIALS = os.path.join(ROOT, "src", "partials")

COUNTRIES = {
    "center-philippines": {
        "flag": "&#127477;&#127469;",
        "name": "Philippines",
        "slug": "center-philippines",
        "tagline": "The flagship center",
        "lede": "Where Cloudstaff's story began in 2005 &mdash; today our largest workforce, our world-class secure campuses, and the deepest bench of outsourcing talent anywhere in our network.",
        "glance": [
            ("Time zone", "UTC+8"),
            ("Shift pattern", "US-aligned standard"),
            ("English", "Top of Asia"),
            ("Experience", "20+ years"),
        ],
        "benefits": [
            ("fa-award", "Two decades of BPO depth", "The most mature center in our network, with proven playbooks for scaling finance, support, and back-office teams for global clients."),
            ("fa-comment", "High English proficiency", "The Philippines consistently ranks at the top of Asia for English fluency, with neutral accents suited to client-facing and stakeholder roles."),
            ("fa-heart", "Famous service culture", "A warm, service-first work culture that clients consistently cite as the reason their customers notice the difference."),
            ("fa-clock", "US hours as standard", "Over 70% of Cloudstaff professionals already work US-aligned shifts &mdash; night-shift operations here are routine, not an exception."),
            ("fa-building-shield", "World-class secure campuses", "Purpose-built facilities with managed devices, biometric access, redundant power and connectivity, transport, and staff-care programs."),
            ("fa-people-group", "The deepest talent pool", "The widest range of roles and the largest candidate network in our footprint &mdash; from entry-level support to senior specialists."),
        ],
        "goodfor": [
            ("fa-chart-pie", "Accounting &amp; Finance", "Bookkeepers, accountants, AP/AR, payroll, financial reporting."),
            ("fa-headset", "Customer &amp; Technical Support", "Voice, chat, email, and tiered technical support teams."),
            ("fa-user-tie", "Executive &amp; Admin Support", "Executive assistants, virtual assistants, back-office coordinators."),
            ("fa-laptop-code", "IT &amp; Helpdesk", "Service desk, provisioning, network and systems support."),
            ("fa-list-check", "Data &amp; Shared Services", "Data entry, document processing, shared-service operations."),
            ("fa-heart-pulse", "Healthcare Support", "Medical billing, coding, and patient administration."),
        ],
        "coverage": "On UTC+8, Philippines teams run your overnight hours as a standard day shift &mdash; and routinely flip to full US-aligned schedules (EST/PST) for real-time coverage of your business day.",
    },
    "center-colombia": {
        "flag": "&#127464;&#127476;",
        "name": "Colombia",
        "slug": "center-colombia",
        "tagline": "Nearshore, in real time",
        "lede": "Latin America's leading outsourcing destination &mdash; university-educated, genuinely bilingual professionals who share your working day and your business culture.",
        "glance": [
            ("Time zone", "UTC-5"),
            ("Overlap", "Same-day, real-time"),
            ("Languages", "Spanish + English"),
            ("Model", "Nearshore"),
        ],
        "benefits": [
            ("fa-clock", "Work in real time, not overtime", "EST and CST overlap means same-day collaboration, faster decisions, and quicker project delivery &mdash; no waiting overnight for answers."),
            ("fa-comment", "Bilingual talent that converts", "Genuinely bilingual Spanish-English professionals who connect with and sell to audiences across the Americas."),
            ("fa-award", "University-educated workforce", "A deep pool of degree-qualified professionals, supported by strong local government backing for the outsourcing sector."),
            ("fa-people-group", "Shared culture, shared success", "Strong cultural alignment with North American and European business norms makes integration fast and friction-free."),
            ("fa-scale-balanced", "Competitive cost base", "Meaningful savings versus onshore hiring while staying in your time zone &mdash; the best of nearshore economics."),
            ("fa-building-shield", "Stable, reliable foundation", "Modern infrastructure, reliable connectivity, and the same managed-device security standard as every Cloudstaff center."),
        ],
        "goodfor": [
            ("fa-headset", "Bilingual Customer Support", "Spanish/English contact-center and customer-care teams."),
            ("fa-arrow-up-right-dots", "Sales &amp; Lead Generation", "SDRs, appointment setters, inside sales, lead gen."),
            ("fa-chart-pie", "Finance &amp; Accounting", "Accountants, AP/AR, bookkeeping, back-office finance."),
            ("fa-scale-balanced", "Legal Support", "Paralegals, document review, legal administration."),
            ("fa-palette", "Digital Marketing", "Social media, content, campaign and community management."),
            ("fa-laptop-code", "IT &amp; Software", "Developers, QA, and technical support roles."),
        ],
        "coverage": "On UTC-5, Colombia sits inside your working day. Your morning stand-up is their morning stand-up &mdash; ideal for roles that need live back-and-forth rather than overnight handoffs.",
    },
    "center-india": {
        "flag": "&#127470;&#127475;",
        "name": "India",
        "slug": "center-india",
        "tagline": "The engineering powerhouse",
        "lede": "One of the world's largest and deepest technical talent pools, backed by a mature STEM and IT ecosystem &mdash; the center of gravity for complex, build-heavy work.",
        "glance": [
            ("Time zone", "UTC+5:30"),
            ("Focus", "Engineering &amp; tech"),
            ("Talent pool", "Among world's largest"),
            ("Ecosystem", "Deep STEM / IT"),
        ],
        "benefits": [
            ("fa-code", "Software engineering at scale", "Front-end, back-end, full-stack, mobile, and 70+ specialist stacks &mdash; the depth to staff whole engineering functions, not just single seats."),
            ("fa-microchip-ai", "AI &amp; machine learning capability", "A fast-growing pool of AI/ML engineers, data scientists, and prompt engineers to build and run intelligent workflows."),
            ("fa-people-group", "Enormous technical talent pool", "One of the largest technically skilled workforces on earth, so even scarce or niche skills can be sourced at depth."),
            ("fa-layer-group", "Mature STEM &amp; IT ecosystem", "Decades of global technology delivery mean established engineering discipline, tooling, and process maturity."),
            ("fa-chart-mixed", "Complex back office &amp; analytics", "Beyond engineering: sophisticated finance operations, data, and analytics for global businesses."),
            ("fa-scale-balanced", "Strong value on high-skill roles", "Access senior technical capability at a fraction of onshore cost, where the savings per role are greatest."),
        ],
        "goodfor": [
            ("fa-code", "Software Development", "Full-stack, mobile, ERP/CRM, and specialist stacks."),
            ("fa-microchip-ai", "AI &amp; Machine Learning", "ML engineers, data scientists, AI/prompt engineers."),
            ("fa-network-wired", "Cloud &amp; Infrastructure", "Cloud, DevOps, infrastructure and platform engineers."),
            ("fa-shield-check", "Cybersecurity", "Security analysts, penetration testers, compliance."),
            ("fa-chart-mixed", "Data &amp; Analytics", "BI, data engineering, reporting and analytics."),
            ("fa-chart-pie", "Complex Accounting", "Fund, corporate, and technical accounting at scale."),
        ],
        "coverage": "On UTC+5:30, India's working day overlaps UK and European hours and reaches into the US morning &mdash; a strong fit for engineering teams that collaborate on a daily cadence rather than live chat.",
    },
    "center-kenya": {
        "flag": "&#127472;&#127466;",
        "name": "Kenya",
        "slug": "center-kenya",
        "tagline": "The rising talent hub",
        "lede": "Young, tech-savvy, English-fluent professionals &mdash; more than 50,000 STEM graduates a year &mdash; positioned on GMT+3 for natural UK and European coverage.",
        "glance": [
            ("Time zone", "UTC+3"),
            ("STEM grads", "50,000+ / year"),
            ("English", "Fluent"),
            ("Coverage", "UK / EU hours"),
        ],
        "benefits": [
            ("fa-graduation-cap", "50,000+ STEM graduates a year", "A large, fast-growing pipeline of technically educated young professionals entering the workforce annually."),
            ("fa-bolt", "Young, tech-savvy workforce", "A digitally native generation that adopts new tools and ways of working quickly."),
            ("fa-comment", "English-fluent, Western-aligned", "Professionals fluent in English and deeply attuned to Western business culture and standards."),
            ("fa-clock", "Natural UK &amp; EU coverage", "On GMT+3, Kenya delivers European business-hours coverage with strong overlap into the US morning."),
            ("fa-scale-balanced", "Up to 70% cost savings", "Among the strongest cost-to-quality ratios in our network, without sacrificing standards."),
            ("fa-arrow-up-right-dots", "Emerging, high-growth market", "An ambitious, rapidly developing outsourcing hub &mdash; an early-mover advantage for forward-looking teams."),
        ],
        "goodfor": [
            ("fa-laptop-code", "IT &amp; Software Development", "Developers, support engineers, and technical roles."),
            ("fa-magnifying-glass-user", "Research", "Market, data, and business research specialists."),
            ("fa-chart-pie", "Accounting &amp; Finance", "Accountants, bookkeeping, and finance operations."),
            ("fa-scale-balanced", "Legal &amp; Compliance", "Legal process, compliance, and document roles."),
            ("fa-palette", "Digital Marketing &amp; Content", "Content creation, social, and campaign support."),
            ("fa-headset", "Customer Support", "English-language customer-service teams."),
        ],
        "coverage": "On UTC+3, Kenya covers the full UK and European working day and opens strong overlap with the US East Coast morning &mdash; ideal for European-hours support and research.",
    },
}

OTHER_LINKS = {
    "center-philippines": [("center-colombia", "&#127464;&#127476; Colombia"), ("center-india", "&#127470;&#127475; India"), ("center-kenya", "&#127472;&#127466; Kenya")],
    "center-colombia": [("center-philippines", "&#127477;&#127469; Philippines"), ("center-india", "&#127470;&#127475; India"), ("center-kenya", "&#127472;&#127466; Kenya")],
    "center-india": [("center-philippines", "&#127477;&#127469; Philippines"), ("center-colombia", "&#127464;&#127476; Colombia"), ("center-kenya", "&#127472;&#127466; Kenya")],
    "center-kenya": [("center-philippines", "&#127477;&#127469; Philippines"), ("center-colombia", "&#127464;&#127476; Colombia"), ("center-india", "&#127470;&#127475; India")],
}


def page(c):
    glance = "\n".join(
        f'        <div class="stat-tile"><div class="stat-tile-label">{lbl}</div>'
        f'<div class="stat-tile-value stat-tile-value-text">{val}</div></div>'
        for lbl, val in c["glance"])
    benefits = "\n".join(
        f'''        <div class="feature-tile">
          <div class="feature-tile-icon"><i class="fa-light {ic}" aria-hidden="true"></i></div>
          <h3>{t}</h3>
          <p>{d}</p>
        </div>''' for ic, t, d in c["benefits"])
    goodfor = "\n".join(
        f'''        <div class="card">
          <h3><i class="fa-light {ic}" aria-hidden="true"></i> {t}</h3>
          <p>{d}</p>
        </div>''' for ic, t, d in c["goodfor"])
    others = "\n".join(
        f'          <a href="{{{{URL:{s}}}}}" class="button button-secondary">{lbl}</a>'
        for s, lbl in OTHER_LINKS[c["slug"]])
    return f'''<section class="site-hero site-hero-dark center-hero">
  <div class="site-band-inner">
    <div class="site-hero-copy">
    <span class="eyebrow"><a href="{{{{URL:international}}}}" class="center-back">International Services Centers</a> &rarr; {c["name"]}</span>
    <div class="center-flag" aria-hidden="true">{c["flag"]}</div>
    <h1>{c["name"]} &mdash; {c["tagline"]}</h1>
    <p>{c["lede"]}</p>
    <a href="{{{{URL:contact}}}}" class="button button-lg">Build a team in {c["name"]}</a>
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <span class="eyebrow">At a glance</span>
    <h2>{c["name"]} at a glance</h2>
    <div class="grid-4 center-glance">
{glance}
    </div>
  </div>
</section>

<section class="site-band site-band-tinted">
  <div class="site-band-inner">
    <span class="eyebrow">Why {c["name"]}</span>
    <h2>The benefits</h2>
    <div class="grid-3">
{benefits}
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <span class="eyebrow">Good for</span>
    <h2>Roles this center does best</h2>
    <p>Every center can staff across our full range of 600+ roles. These are the functions {c["name"]} is especially strong in &mdash; where its talent pool, skills, and time zone line up best.</p>
    <div class="grid-3">
{goodfor}
    </div>
    <p><a href="{{{{URL:team-builder}}}}" class="button-link">Build a {c["name"]} team in the Team Builder &rarr;</a></p>
  </div>
</section>

<section class="site-band site-band-tinted">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">Follow the sun</span>
      <h2>How {c["name"]} fits your day</h2>
      <p>{c["coverage"]}</p>
      <p><a href="{{{{URL:international}}}}" class="button-link">See the full coverage chart &rarr;</a></p>
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <span class="eyebrow">Explore the network</span>
    <h2>Our other International Services Centers</h2>
    <div class="cluster center-others">
{others}
    </div>
  </div>
</section>

<section class="site-cta">
  <div class="site-band-inner">
    <h2>Ready to build your {c["name"]} team?</h2>
    <p>Tell us the roles and hours you need &mdash; we'll show you how a {c["name"]} team fits.</p>
    <a href="{{{{URL:contact}}}}" class="button button-inverse button-lg">Talk to an Expert</a>
  </div>
</section>
'''


for slug, c in COUNTRIES.items():
    open(os.path.join(PARTIALS, f"{slug}.html"), "w").write(page(c))
    print("wrote", slug)
