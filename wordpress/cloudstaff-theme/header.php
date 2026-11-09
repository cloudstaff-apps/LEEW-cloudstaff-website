<?php
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
<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header">
  <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="site-header-brand" aria-label="Cloudstaff — home"><img class="site-logo-img" src="<?php echo esc_url( get_template_directory_uri() . '/cloudstaff-logo.png' ); ?>" alt="Cloudstaff" width="1329" height="372" decoding="async"></a>
  <nav class="site-nav" aria-label="Main navigation">
    <div class="site-nav-item">
      <a href="<?php echo esc_url( home_url( '/what-is-remote-staffing/' ) ); ?>" <?php if ( is_page( 'what-is-remote-staffing' ) ) echo 'aria-current="page"'; ?> class="site-nav-parent">About<span class="site-nav-caret" aria-hidden="true"></span></a>
      <div class="site-nav-dropdown">
        <a href="<?php echo esc_url( home_url( '/what-is-remote-staffing/' ) ); ?>" <?php if ( is_page( 'what-is-remote-staffing' ) ) echo 'aria-current="page"'; ?>>What Is Remote Staffing?</a>
        <a href="<?php echo esc_url( home_url( '/how-it-works/' ) ); ?>" <?php if ( is_page( 'how-it-works' ) ) echo 'aria-current="page"'; ?>>How It Works</a>
        <a href="<?php echo esc_url( home_url( '/timezones/' ) ); ?>" <?php if ( is_page( 'timezones' ) ) echo 'aria-current="page"'; ?>>Time Zones</a>
        <a href="<?php echo esc_url( home_url( '/why-cloudstaff/' ) ); ?>" <?php if ( is_page( 'why-cloudstaff' ) ) echo 'aria-current="page"'; ?>>Why Cloudstaff</a>
        <a href="<?php echo esc_url( home_url( '/security/' ) ); ?>" <?php if ( is_page( 'security' ) ) echo 'aria-current="page"'; ?>>Security</a>
        <a href="<?php echo esc_url( home_url( '/customers/' ) ); ?>" <?php if ( is_page( 'customers' ) ) echo 'aria-current="page"'; ?>>Customers</a>
      </div>
    </div>
    <div class="site-nav-item">
      <a href="<?php echo esc_url( home_url( '/roles/' ) ); ?>" <?php if ( is_page( 'roles' ) ) echo 'aria-current="page"'; ?> class="site-nav-parent">Roles &amp; Industries<span class="site-nav-caret" aria-hidden="true"></span></a>
      <div class="site-nav-dropdown">
        <a href="<?php echo esc_url( home_url( '/roles/' ) ); ?>" <?php if ( is_page( 'roles' ) ) echo 'aria-current="page"'; ?>>All roles &amp; industries</a>
        <a href="<?php echo esc_url( home_url( '/team-builder/' ) ); ?>" <?php if ( is_page( 'team-builder' ) ) echo 'aria-current="page"'; ?>>Team Builder</a>
        <a href="<?php echo esc_url( home_url( '/pricing/' ) ); ?>" <?php if ( is_page( 'pricing' ) ) echo 'aria-current="page"'; ?>>Pricing &amp; Savings</a>
      </div>
    </div>
    <a href="<?php echo esc_url( home_url( '/international/' ) ); ?>" <?php if ( is_page( 'international' ) ) echo 'aria-current="page"'; ?>>International</a>
    <a href="<?php echo esc_url( home_url( '/cfo-guide/' ) ); ?>" <?php if ( is_page( 'cfo-guide' ) ) echo 'aria-current="page"'; ?>>CFO Guide</a>
    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" <?php if ( is_page( 'contact' ) ) echo 'aria-current="page"'; ?>>Contact Us</a>
  </nav>
  <div class="site-header-cta">
    <a href="https://www.cloudstaff.com/careers/" class="button button-quiet" target="_blank" rel="noopener">Jobs at Cloudstaff</a>
    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="button">Talk to an Expert</a>
  </div>
</header>
