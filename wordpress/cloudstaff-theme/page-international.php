<?php
/**
 * Template Name: International
 * Template Post Type: page
 *
 * Generated from src/partials/international.html by build.py — edit the partial,
 * not this file, then re-run `python3 build.py`.
 *
 * @package Cloudstaff
 */

get_header();
?>
<main class="site-main" id="main-content">
<section class="site-hero site-hero-photo" style="--hero-image: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=2000&q=70')" title="Earth at night from space">
  <div class="site-band-inner">
    <div class="site-hero-copy">
    <span class="eyebrow">International Services Centers</span>
    <h1>Global reach, local teams</h1>
    <p>Cloudstaff operates International Services Centers across four continents, the Philippines, Colombia, India, and Kenya, backed by specialist hubs worldwide. One partner, one standard of security and service, with the right talent in the right time zone for your business.</p>
    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="button button-lg">Plan your global team</a>
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <div class="grid-3">
      <div class="feature-tile">
        <div class="feature-tile-icon"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div>
        <h3>Follow the sun</h3>
        <p>With centers spanning UTC-5 to UTC+8, work hands off across time zones, cover your business hours, run night shifts without night work, or keep critical functions moving 24 hours a day.</p>
      </div>
      <div class="feature-tile">
        <div class="feature-tile-icon"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
        <h3>Global reach, local teams</h3>
        <p>Every center is a genuine local operation, local recruiters, local HR, local culture, operating to one global Cloudstaff standard of security, infrastructure, and staff care.</p>
      </div>
      <div class="feature-tile">
        <div class="feature-tile-icon"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3v18"/><path d="M8 21h8"/><path d="M4 7h16"/><path d="m5 7-3 6a3.3 3.3 0 0 0 6 0z"/><path d="m19 7-3 6a3.3 3.3 0 0 0 6 0z"/></svg></div>
        <h3>Balance cost and capability</h3>
        <p>A diversified footprint lets you match each role to the best market for skills, cost, language, and coverage, while reducing single-country operational risk.</p>
      </div>
    </div>
  </div>
</section>

<section class="site-band site-band-tinted">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">Follow the sun</span>
      <h2>Coverage that follows your working day</h2>
      <p>Set your region and choose how you'd like your team to work. The chart shows exactly when each center is online relative to <em>your</em> working day, and what shift that means for them locally.</p>

      <div class="coverage-tool" id="coverage-tool">
        <div class="cov-controls card">
          <div class="cov-control">
            <span class="cov-label">Which hours should your team work?</span>
            <div class="tb-seg" id="cov-mode" role="group" aria-label="Shift preference"></div>
          </div>
          <div class="cov-control">
            <span class="cov-label">Your region</span>
            <div class="tb-seg" id="cov-region" role="group" aria-label="Your region"></div>
          </div>
          <div class="cov-control">
            <label class="cov-label" for="cov-zone">Your time zone</label>
            <select class="select" id="cov-zone" aria-label="Your time zone"></select>
          </div>
        </div>

        <div class="card cov-chart" id="cov-chart" aria-live="polite"></div>
        <p class="cov-note" id="cov-note"></p>
      </div>
    </div>
  </div>
</section>
<script src="<?php echo esc_url( get_template_directory_uri() . '/coverage.js' ); ?>" defer></script>

<section class="site-band">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">Our International Services Centers</span>
      <h2>Four centers, one standard</h2>
      <div class="grid-2">
        <div class="card intl-card">
          <div class="intl-flag"><img class="flag" src="https://flagcdn.com/ph.svg" width="24" height="18" alt="Philippines" loading="lazy" decoding="async"></div>
          <h3>Philippines, the flagship</h3>
          <p class="intl-tagline">Where Cloudstaff's story began, and home to our largest workforce and world-class secure campuses.</p>
          <p>Deep BPO experience, high English proficiency with neutral accents, and a famously strong service culture. US-aligned night shifts are standard practice, supported by full facilities, transport, and staff-care programs.</p>
          <p><strong>Specialisms:</strong> accounting &amp; finance, customer &amp; technical support, executive assistance, data entry, shared services, and 600+ roles across every function.</p>
          <p><a href="<?php echo esc_url( home_url( '/center-philippines/' ) ); ?>" class="button button-sm">Explore Philippines &rarr;</a></p>
        </div>
        <div class="card intl-card">
          <div class="intl-flag"><img class="flag" src="https://flagcdn.com/co.svg" width="24" height="18" alt="Colombia" loading="lazy" decoding="async"></div>
          <h3>Colombia, nearshore, real time</h3>
          <p class="intl-tagline">Work in real time, not overtime: EST/CST overlap for seamless same-day collaboration.</p>
          <p>University-educated, genuinely bilingual professionals whose Spanish-English fluency connects and converts across the Americas, with strong cultural alignment to North American business.</p>
          <p><strong>Specialisms:</strong> bilingual customer support &amp; contact center, finance &amp; accounting, sales &amp; lead generation, legal, back-office operations, digital marketing, IT &amp; software.</p>
          <p><a href="<?php echo esc_url( home_url( '/center-colombia/' ) ); ?>" class="button button-sm">Explore Colombia &rarr;</a></p>
        </div>
        <div class="card intl-card">
          <div class="intl-flag"><img class="flag" src="https://flagcdn.com/in.svg" width="24" height="18" alt="India" loading="lazy" decoding="async"></div>
          <h3>India, the engineering powerhouse</h3>
          <p class="intl-tagline">One of the world's largest technically skilled talent pools, backed by a deep STEM ecosystem.</p>
          <p>The center of gravity for complex technical delivery: software engineering at scale, AI/ML capability, and sophisticated finance and back-office operations for global clients.</p>
          <p><strong>Specialisms:</strong> software development, AI &amp; machine learning engineering, complex back office, accounting, data &amp; analytics.</p>
          <p><a href="<?php echo esc_url( home_url( '/center-india/' ) ); ?>" class="button button-sm">Explore India &rarr;</a></p>
        </div>
        <div class="card intl-card">
          <div class="intl-flag"><img class="flag" src="https://flagcdn.com/ke.svg" width="24" height="18" alt="Kenya" loading="lazy" decoding="async"></div>
          <h3>Kenya, the rising talent hub</h3>
          <p class="intl-tagline">Young, tech-savvy, English-fluent talent, 50,000+ STEM graduates every year.</p>
          <p>On GMT+3, Kenya delivers natural UK and European business-hours coverage and strong US-morning overlap, with professionals deeply attuned to Western business culture and savings of up to 70%.</p>
          <p><strong>Specialisms:</strong> IT &amp; software development, research, accounting &amp; finance, legal process &amp; compliance, e-commerce, digital marketing &amp; content, healthcare support.</p>
          <p><a href="<?php echo esc_url( home_url( '/center-kenya/' ) ); ?>" class="button button-sm">Explore Kenya &rarr;</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="site-band site-band-tinted site-band-reverse">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">Local presence, international reach</span>
      <h2>Client teams where you are, delivery teams where the talent is</h2>
      <p>Your relationship with Cloudstaff is local: client-facing teams in Charlotte, Houston, and Dallas in the US, Sydney and Brisbane in Australia, and London in the UK. Behind them stands the international delivery network, so you get local accountability with global capability.</p>
      <p>Beyond the four International Services Centers, specialist hubs extend coverage, languages, and niche skills across the globe.</p>
    </div>
    <div class="site-visual">
      <div class="card">
        <h3>Specialist hubs</h3>
        <div class="cluster intl-hubs">
          <span class="badge"><img class="flag" src="https://flagcdn.com/za.svg" width="24" height="18" alt="South Africa" loading="lazy" decoding="async"> South Africa</span>
          <span class="badge"><img class="flag" src="https://flagcdn.com/ni.svg" width="24" height="18" alt="Nicaragua" loading="lazy" decoding="async"> Nicaragua</span>
          <span class="badge"><img class="flag" src="https://flagcdn.com/my.svg" width="24" height="18" alt="Malaysia" loading="lazy" decoding="async"> Malaysia</span>
          <span class="badge"><img class="flag" src="https://flagcdn.com/sg.svg" width="24" height="18" alt="Singapore" loading="lazy" decoding="async"> Singapore</span>
          <span class="badge"><img class="flag" src="https://flagcdn.com/vn.svg" width="24" height="18" alt="Vietnam" loading="lazy" decoding="async"> Vietnam</span>
          <span class="badge"><img class="flag" src="https://flagcdn.com/jp.svg" width="24" height="18" alt="Japan" loading="lazy" decoding="async"> Japan</span>
          <span class="badge"><img class="flag" src="https://flagcdn.com/lk.svg" width="24" height="18" alt="Sri Lanka" loading="lazy" decoding="async"> Sri Lanka</span>
        </div>
        <h3 class="intl-offices-h">Client offices</h3>
        <div class="cluster intl-hubs">
          <span class="badge badge-success"><img class="flag" src="https://flagcdn.com/us.svg" width="24" height="18" alt="United States" loading="lazy" decoding="async"> Charlotte &middot; Houston &middot; Dallas</span>
          <span class="badge badge-success"><img class="flag" src="https://flagcdn.com/au.svg" width="24" height="18" alt="Australia" loading="lazy" decoding="async"> Sydney &middot; Brisbane</span>
          <span class="badge badge-success"><img class="flag" src="https://flagcdn.com/gb.svg" width="24" height="18" alt="United Kingdom" loading="lazy" decoding="async"> London</span>
        </div>
        <p class="intl-hubs-cta"><a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="button">Contact us about global coverage &rarr;</a></p>
      </div>
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">Why it matters</span>
      <h2>A diversified footprint is a risk strategy</h2>
      <div class="grid-3">
        <div class="card">
          <div class="step-number"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3 3.5 3 14.5 0 18"/><path d="M12 3c-3 3.5-3 14.5 0 18"/></svg></div>
          <h3>Continuity by design</h3>
          <p>Multiple centers mean weather, power, or regional events in one country never take your operation offline, work can shift across the network.</p>
        </div>
        <div class="card">
          <div class="step-number"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m17 11 4-4-4-4"/><path d="M21 7H9"/><path d="m7 13-4 4 4 4"/><path d="M3 17h12"/></svg></div>
          <h3>The right market per role</h3>
          <p>Bilingual sales in Bogot&aacute;, engineering in Bangalore, accounting in Clark, UK-hours support in Nairobi, each role goes where the talent is deepest.</p>
        </div>
        <div class="card">
          <div class="step-number"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg></div>
          <h3>One security standard</h3>
          <p>Every center runs the same managed devices, ISO-certified controls, monitored facilities, and business continuity plans, audited centrally.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="site-cta">
  <div class="site-band-inner">
    <h2>Build a team the sun never sets on</h2>
    <p>Tell us your hours, your roles, and your growth plans, and we'll map them to the right centers.</p>
    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="button button-inverse button-lg">Plan your global team</a>
  </div>
</section>

</main>
<?php
get_footer();
