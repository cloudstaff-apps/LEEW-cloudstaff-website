<?php
/**
 * Template Name: Time Zones
 * Template Post Type: page
 *
 * Generated from src/partials/timezones.html by build.py — edit the partial,
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
    <span class="eyebrow">Follow the sun</span>
    <h1>Time zones &amp; coverage</h1>
    <p>With International Services Centers spanning UTC-5 to UTC+8, Cloudstaff can cover your business hours in real time, run your overnight shifts without night work, or keep critical functions moving around the clock. Set your region below to see exactly when each center is online for you.</p>
    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="button button-lg">Plan your coverage</a>
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">Interactive tool</span>
      <h2>Coverage that follows your working day</h2>
      <p>Set your region and choose how you'd like your team to work &mdash; the chart shows exactly when each center is online relative to <em>your</em> working day, and what shift that means for them locally.</p>

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

<section class="site-band site-band-tinted">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">Three ways to use the clock</span>
      <h2>Make time zones work for you</h2>
      <div class="grid-3">
        <div class="feature-tile">
          <div class="feature-tile-icon"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div>
          <h3>Cover your business hours</h3>
          <p>Have your team work your 9&ndash;5 directly. Nearshore Colombia does it on a normal day shift; the Philippines, India, and Kenya run it as a fully supported evening or night shift.</p>
        </div>
        <div class="feature-tile">
          <div class="feature-tile-icon"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/><path d="M3 21v-5h5"/></svg></div>
          <h3>Run work overnight</h3>
          <p>Hand off at the end of your day and pick it up finished. Offshore day shifts land in your overnight hours &mdash; so routine processing happens while your local team sleeps.</p>
        </div>
        <div class="feature-tile">
          <div class="feature-tile-icon"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3 3.5 3 14.5 0 18"/><path d="M12 3c-3 3.5-3 14.5 0 18"/></svg></div>
          <h3>Keep going 24 hours</h3>
          <p>Combine centers across UTC-5 to UTC+8 to keep critical functions &mdash; support, monitoring, operations &mdash; moving around the clock, with one security standard worldwide.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="site-cta">
  <div class="site-band-inner">
    <h2>Build a team the sun never sets on</h2>
    <p>Tell us your hours, your roles, and your growth plans &mdash; we'll map them to the right centers and the right shifts.</p>
    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="button button-inverse button-lg">Plan your coverage</a>
  </div>
</section>

</main>
<?php
get_footer();
