"""Inline SVG icon set + hero artwork + logo for the Cloudstaff site build.

Icons are 24x24 stroke glyphs (currentColor) so they inherit text color and
need no external font. build.py replaces <i class="fa-light fa-NAME"...></i>
with the mapped inline SVG, and {{ART:name}} with a generated hero artwork.
"""

# --- 24x24 stroke glyph inner markup ---------------------------------------
GLYPHS = {
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "user-check": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="m16 11 2 2 4-4"/>',
    "user-search": '<circle cx="10" cy="7" r="4"/><path d="M10.3 15H7a4 4 0 0 0-4 4v2"/><circle cx="17" cy="17" r="3"/><path d="m21 21-1.9-1.9"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "shield-check": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "key": '<circle cx="7.5" cy="15.5" r="4.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/>',
    "clipboard-check": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "list-check": '<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z"/><path d="M14 2v5h5"/><path d="M9 13h6"/><path d="M9 17h6"/>',
    "banknote": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01"/><path d="M18 12h.01"/>',
    "laptop-code": '<path d="M3 19h18"/><rect x="4" y="5" width="16" height="11" rx="2"/><path d="m10 9-1.5 1.5L10 12"/><path d="m14 9 1.5 1.5L14 12"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "headphones": '<path d="M3 14v-3a9 9 0 0 1 18 0v3"/><rect x="3" y="14" width="4" height="6" rx="2"/><rect x="17" y="14" width="4" height="6" rx="2"/>',
    "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
    "refresh": '<path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/><path d="M3 21v-5h5"/>',
    "left-right": '<path d="m17 11 4-4-4-4"/><path d="M21 7H9"/><path d="m7 13-4 4 4 4"/><path d="M3 17h12"/>',
    "trending-up": '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
    "pie": '<path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/>',
    "bar-chart": '<path d="M3 3v18h18"/><path d="M7 15v-4"/><path d="M12 15V7"/><path d="M17 15v-6"/>',
    "gauge": '<path d="m12 14 3.5-3.5"/><path d="M20.3 18a9 9 0 1 0-16.6 0"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h6.5a3.5 3.5 0 0 0 0-7h-5a3.5 3.5 0 0 1 0-7H16"/>',
    "network": '<rect x="9" y="2" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="16" y="16" width="6" height="6" rx="1"/><path d="M12 8v3"/><path d="M5 16v-3h14v3"/>',
    "chip": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4"/><path d="M15 2v4"/><path d="M9 18v4"/><path d="M15 18v4"/><path d="M2 9h4"/><path d="M2 15h4"/><path d="M18 9h4"/><path d="M18 15h4"/>',
    "bot": '<rect x="4" y="8" width="16" height="12" rx="2"/><path d="M12 4v4"/><circle cx="12" cy="3" r="1"/><circle cx="9" cy="13" r="1"/><circle cx="15" cy="13" r="1"/><path d="M2 14h2"/><path d="M20 14h2"/>',
    "sparkles": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
    "palette": '<path d="M12 22a10 10 0 1 1 10-10c0 2-1.5 3.5-3.5 3.5H16a2 2 0 0 0-2 2c0 1.5.5 4.5-2 4.5z"/><circle cx="7.5" cy="10.5" r="1"/><circle cx="12" cy="7.5" r="1"/><circle cx="16.5" cy="10.5" r="1"/>',
    "code": '<path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="1"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M12 6h.01"/><path d="M16 6h.01"/><path d="M8 10h.01"/><path d="M12 10h.01"/><path d="M16 10h.01"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/>',
    "grad": '<path d="m22 9-10-5L2 9l10 5 10-5z"/><path d="M6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5"/><path d="M22 9v6"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="m9 14.2-1 7.8 4-2.5 4 2.5-1-7.8"/>',
    "trophy": '<path d="M8 21h8"/><path d="M12 17v4"/><path d="M7 4h10v6a5 5 0 0 1-10 0z"/><path d="M7 6H4a2 2 0 0 0 2 5h1"/><path d="M17 6h3a2 2 0 0 1-2 5h-1"/>',
    "heart": '<path d="M19.5 13.5 12 21l-7.5-7.5a5 5 0 1 1 7.5-6.6 5 5 0 1 1 7.5 6.6z"/>',
    "heart-pulse": '<path d="M19.5 13.5 12 21l-7.5-7.5a5 5 0 1 1 7.5-6.6 5 5 0 1 1 7.5 6.6z"/><path d="M7 12h2.5l1.5-2.5 2 5 1.5-2.5H17"/>',
    "party": '<path d="M5.5 11 2 22l11-3.5z"/><path d="M14 10 22 2"/><path d="M9.5 14.5 12 12"/><path d="M17 6h.01"/><path d="M21 12h.01"/><path d="M15 2h.01"/><path d="M20 17h.01"/>',
    "scale": '<path d="M12 3v18"/><path d="M8 21h8"/><path d="M4 7h16"/><path d="m5 7-3 6a3.3 3.3 0 0 0 6 0z"/><path d="m19 7-3 6a3.3 3.3 0 0 0 6 0z"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 12 10 5 10-5"/><path d="m2 17 10 5 10-5"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    "star": '<path d="m12 2 2.9 6.6 7.1.7-5.3 4.7 1.6 7-6.3-3.7L5.7 21l1.6-7L2 9.3l7.1-.7z"/>',
    "calculator": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8"/><path d="M8 11h.01"/><path d="M12 11h.01"/><path d="M16 11h.01"/><path d="M8 15h.01"/><path d="M12 15h.01"/><path d="M16 15h.01"/><path d="M8 19h8"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3 3.5 3 14.5 0 18"/><path d="M12 3c-3 3.5-3 14.5 0 18"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>',
    "comment": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8z"/>',
}

# --- fa-name -> glyph mapping ------------------------------------------------
FA_MAP = {
    "fa-user": "user",
    "fa-user-tie": "user",
    "fa-user-crown": "star",
    "fa-user-check": "user-check",
    "fa-user-shield": "shield-check",
    "fa-user-dollar": "banknote",
    "fa-users": "users",
    "fa-people-group": "users",
    "fa-magnifying-glass-user": "user-search",
    "fa-shield-check": "shield-check",
    "fa-shield-halved": "shield",
    "fa-building-shield": "building",
    "fa-key": "key",
    "fa-database": "database",
    "fa-clipboard-check": "clipboard-check",
    "fa-clipboard-list-check": "clipboard-check",
    "fa-list-check": "list-check",
    "fa-file-lines": "file",
    "fa-file-invoice-dollar": "banknote",
    "fa-money-check-dollar": "banknote",
    "fa-laptop-code": "laptop-code",
    "fa-laptop-binary": "laptop-code",
    "fa-laptop-mobile": "laptop-code",
    "fa-mobile-screen": "phone",
    "fa-headset": "headphones",
    "fa-bolt": "zap",
    "fa-plug-circle-bolt": "zap",
    "fa-arrows-rotate": "refresh",
    "fa-arrows-left-right": "left-right",
    "fa-chart-line-up": "trending-up",
    "fa-arrow-up-right-dots": "trending-up",
    "fa-chart-pie": "pie",
    "fa-chart-mixed": "bar-chart",
    "fa-gauge-high": "gauge",
    "fa-clock": "clock",
    "fa-route": "route",
    "fa-road": "route",
    "fa-diagram-project": "network",
    "fa-network-wired": "network",
    "fa-microchip-ai": "chip",
    "fa-robot": "bot",
    "fa-wand-magic-sparkles": "sparkles",
    "fa-palette": "palette",
    "fa-code": "code",
    "fa-building": "building",
    "fa-graduation-cap": "grad",
    "fa-award": "award",
    "fa-trophy": "trophy",
    "fa-certificate": "award",
    "fa-heart": "heart",
    "fa-hand-holding-heart": "heart",
    "fa-heart-pulse": "heart-pulse",
    "fa-champagne-glasses": "party",
    "fa-scale-balanced": "scale",
    "fa-layer-group": "layers",
    "fa-grid-2": "grid",
    "fa-chess": "compass",
    "fa-globe": "globe",
    "fa-comment": "comment",
    "fa-compass": "compass",
    "fa-bullseye-arrow": "target",
    "fa-calculator": "calculator",
    "fa-file": "file",
}


def icon_svg(glyph, cls="icon"):
    inner = GLYPHS[glyph]
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{inner}</svg>')


# --- Hero artwork ------------------------------------------------------------
# Deterministic decorative panel: gradient field, rings, floating dots, and a
# large central glyph. Colors come from CSS custom properties so partner
# rebrands cascade automatically.
_DOTS = [(52, 84, 5), (108, 40, 3.5), (356, 62, 4.5), (396, 150, 3),
         (60, 300, 4), (150, 352, 3), (330, 330, 5), (398, 262, 3.5),
         (30, 190, 3), (218, 30, 3)]


def hero_art(glyph):
    dots = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" class="art-dot"/>' for x, y, r in _DOTS)
    inner = GLYPHS[glyph]
    return f'''<svg class="hero-art" viewBox="0 0 440 400" fill="none" aria-hidden="true" focusable="false" role="img">
  <defs>
    <linearGradient id="art-bg-{glyph}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" class="art-grad-a"/>
      <stop offset="1" class="art-grad-b"/>
    </linearGradient>
  </defs>
  <rect x="8" y="8" width="424" height="384" rx="36" fill="url(#art-bg-{glyph})"/>
  <circle cx="220" cy="200" r="128" class="art-ring" stroke-width="2"/>
  <circle cx="220" cy="200" r="168" class="art-ring art-ring-faint" stroke-width="1.5"/>
  {dots}
  <g transform="translate(136 116) scale(7)" class="art-glyph" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none">{inner}</g>
</svg>'''


# --- Logo --------------------------------------------------------------------
# Faithful recreation of the Cloudstaff lockup: brand-blue circle emblem with
# the white two-bump cloud (wavy base), plus the "Cloudstaff" wordmark in the
# brand heading font. Wordmark color flips for dark surfaces via CSS.
_CLOUD_EMBLEM = (
    '<circle cx="24" cy="24" r="24" class="site-logo-disc"/>'
    '<path class="site-logo-cloud-shape" d="M12.2 30.2c-2.3-.6-3.4-3.2-2.1-5.2'
    '.8-1.2 2.2-1.8 3.6-1.5.2-2.4 2.2-4.3 4.7-4.3 1.5 0 2.9.7 3.8 1.9 1.3-2.9'
    ' 4.2-4.8 7.5-4.8 4.6 0 8.3 3.7 8.3 8.3 0 1.5-.4 3-1.2 4.2-.3.4-.8.7-1.3.7'
    '-3.6.3-7.2-.7-10.8-1-4.2-.4-8.4 2.6-12.5 1.7z"/>')


def logo(variant="default"):
    cls = "site-logo site-logo-light" if variant == "light" else "site-logo"
    return (f'<span class="{cls}">'
            f'<svg class="site-logo-emblem" viewBox="0 0 48 48" aria-hidden="true" '
            f'focusable="false">{_CLOUD_EMBLEM}</svg>'
            f'<span class="site-logo-word">Cloudstaff<sup>&reg;</sup></span></span>')


# --- Certification seals (recreated from the CFO Kit's stylised marks) ------
# Uniform seal: outer ring, dotted inner ring, small glyph, monogram, subline.
CERT_SEALS = {
    "iso27001":  {"glyph": "shield-check", "mono": "27001", "top": "ISO/IEC", "sub": "2022"},
    "iso9001":   {"glyph": "award",        "mono": "9001",  "top": "ISO",     "sub": "2015"},
    "soc2":      {"glyph": "clipboard-check", "mono": "SOC 2", "top": "ALIGNED", "sub": "CONTROLS"},
    "gdpr":      {"glyph": "star",         "mono": "GDPR",  "top": "EU",      "sub": "ALIGNED"},
    "hipaa":     {"glyph": "heart-pulse",  "mono": "HIPAA", "top": "US",      "sub": "ALIGNED"},
    "pcidss":    {"glyph": "banknote",     "mono": "PCI DSS", "top": "PAYMENTS", "sub": "ALIGNED"},
    "e8":        {"glyph": "shield",       "mono": "E8",    "top": "ESSENTIAL", "sub": "EIGHT"},
    "cssecure":  {"glyph": "key",          "mono": "SECURE", "top": "CLOUDSTAFF", "sub": "FRAMEWORK"},
    "scorecard": {"glyph": "gauge",        "mono": "A",     "top": "SECURITYSCORECARD", "sub": "99.9"},
    "years20":   {"glyph": "trophy",       "mono": "20",    "top": "YEARS OF", "sub": "EXCELLENCE"},
}


def cert_seal(key):
    s = CERT_SEALS[key]
    glyph = GLYPHS[s["glyph"]]
    mono = s["mono"]
    size = 30 if len(mono) <= 2 else (20 if len(mono) <= 4 else 14)
    top_size = 6 if len(s["top"]) > 10 else 7.5
    return f'''<svg class="cert-seal-svg" viewBox="0 0 96 96" aria-hidden="true" focusable="false">
  <circle cx="48" cy="48" r="45" class="seal-face"/>
  <circle cx="48" cy="48" r="45" class="seal-ring" fill="none" stroke-width="2.5"/>
  <circle cx="48" cy="48" r="37" class="seal-dots" fill="none" stroke-width="1" stroke-dasharray="1.5 3.5"/>
  <g transform="translate(41 13) scale(0.6)" class="seal-glyph" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{glyph}</g>
  <text x="48" y="{51 if len(mono) <= 2 else 50}" text-anchor="middle" class="seal-mono" font-size="{size}">{mono}</text>
  <text x="48" y="63" text-anchor="middle" class="seal-top" font-size="{top_size}">{s["top"]}</text>
  <text x="48" y="73" text-anchor="middle" class="seal-sub" font-size="7">{s["sub"]}</text>
</svg>'''


# --- Country flags ----------------------------------------------------------
# Rendered as real flag images (not OS emoji, which fall back to plain letters
# like "PH"/"CO" on Windows). ISO 3166-1 alpha-2 codes; served as SVG.
FLAG_NAMES = {
    "ph": "Philippines", "co": "Colombia", "in": "India", "ke": "Kenya",
    "za": "South Africa", "ni": "Nicaragua", "my": "Malaysia", "sg": "Singapore",
    "vn": "Vietnam", "jp": "Japan", "lk": "Sri Lanka",
    "us": "United States", "au": "Australia", "gb": "United Kingdom",
    "nz": "New Zealand", "sg": "Singapore",
}


def flag(code):
    code = code.lower()
    name = FLAG_NAMES.get(code, code.upper())
    return (f'<img class="flag" src="https://flagcdn.com/{code}.svg" '
            f'width="24" height="18" alt="{name}" loading="lazy" decoding="async">')
