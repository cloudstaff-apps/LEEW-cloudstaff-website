/* Cloudstaff "Follow the sun" coverage tool.
   Shows, on the CLIENT's local 24-hour clock, when each International Services
   Center is online — given the client's region/time zone and whether the team
   works its own local day shift or the client's business day. Each center shows
   BOTH its day shift and the evening/night shift that aligns to the client. */
(function () {
  "use strict";

  var chart = document.getElementById("cov-chart");
  if (!chart) return;

  /* Center UTC offsets (hours) */
  var CENTERS = [
    { key: "co", flag: "🇨🇴", name: "Colombia", off: -5 },
    { key: "ke", flag: "🇰🇪", name: "Kenya", off: 3 },
    { key: "in", flag: "🇮🇳", name: "India", off: 5.5 },
    { key: "ph", flag: "🇵🇭", name: "Philippines", off: 8 }
  ];

  /* Client regions -> zones [label, offset] */
  var REGIONS = {
    usa: { label: "USA", zones: [
      ["Eastern (ET)", -5], ["Central (CT)", -6], ["Mountain (MT)", -7], ["Pacific (PT)", -8] ] },
    aus: { label: "Australia", zones: [
      ["Sydney (AEST)", 10], ["Adelaide (ACST)", 9.5], ["Perth (AWST)", 8] ] },
    eur: { label: "Europe", zones: [
      ["London (GMT)", 0], ["Central Europe (CET)", 1], ["Eastern Europe (EET)", 2] ] }
  };

  var MODES = {
    local: "Their day shift (9–5 local)",
    client: "My business day"
  };

  var state = { mode: "local", region: "usa", zoneIdx: 0 };

  function clientOffset() { return REGIONS[state.region].zones[state.zoneIdx][1]; }

  function mod24(h) { return ((h % 24) + 24) % 24; }

  function fmt(h) {
    h = mod24(h);
    var whole = Math.floor(h);
    var min = Math.round((h - whole) * 60);
    var ampm = whole < 12 ? "am" : "pm";
    var display = whole % 12; if (display === 0) display = 12;
    return display + (min ? ":" + (min < 10 ? "0" + min : min) : "") + ampm;
  }

  /* Build segments for a bar that may wrap past 24h. Returns [{start,len}] */
  function segs(start, len) {
    start = mod24(start);
    if (start + len <= 24) return [{ start: start, len: len }];
    return [{ start: start, len: 24 - start }, { start: 0, len: len - (24 - start) }];
  }

  var SUN = '<svg class="cov-ico" viewBox="0 0 24 24" aria-hidden="true">' +
    '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4' +
    'M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var MOON = '<svg class="cov-ico cov-ico--fill" viewBox="0 0 24 24" aria-hidden="true">' +
    '<path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z"/></svg>';

  /* A labelled shift bar. kind = "day" | "night"; label text sits inside the
     widest segment (so a bar that wraps past midnight still reads cleanly). */
  function shiftBar(start, len, kind, label) {
    var parts = segs(start, len), li = 0, i;
    for (i = 1; i < parts.length; i++) if (parts[i].len > parts[li].len) li = i;
    var icon = kind === "day" ? SUN : MOON;
    return parts.map(function (s, idx) {
      var inner = (idx === li && s.len >= 3.5)
        ? '<span class="cov-bar-label">' + icon + '<span>' + label + '</span></span>' : '';
      return '<div class="cov-bar cov-bar--' + kind + '" style="--start:' + s.start +
        ';--len:' + s.len + '">' + inner + '</div>';
    }).join("");
  }

  /* --- Controls ------------------------------------------------------------ */
  function seg(elId, options, key, onChange) {
    var el = document.getElementById(elId);
    el.innerHTML = "";
    Object.keys(options).forEach(function (k) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "tb-seg-btn" + (state[key] === k ? " is-active" : "");
      b.textContent = options[k];
      b.addEventListener("click", function () {
        state[key] = k;
        el.querySelectorAll(".tb-seg-btn").forEach(function (x) { x.classList.remove("is-active"); });
        b.classList.add("is-active");
        onChange();
      });
      el.appendChild(b);
    });
  }

  function buildRegion() {
    var opts = {};
    Object.keys(REGIONS).forEach(function (r) { opts[r] = REGIONS[r].label; });
    seg("cov-region", opts, "region", function () {
      state.zoneIdx = 0;
      buildZone();
      render();
    });
  }

  function buildZone() {
    var sel = document.getElementById("cov-zone");
    sel.innerHTML = "";
    REGIONS[state.region].zones.forEach(function (z, i) {
      var o = document.createElement("option");
      o.value = i; o.textContent = z[0];
      if (i === state.zoneIdx) o.selected = true;
      sel.appendChild(o);
    });
    sel.onchange = function () { state.zoneIdx = parseInt(sel.value, 10); render(); };
  }

  /* --- Render -------------------------------------------------------------- */
  function render() {
    var co = clientOffset();
    var rows = "";

    /* Client business day reference row (9-17 client local) */
    rows += '<div class="cov-row cov-row-you">' +
      '<span class="cov-name">Your business day <small>9am–5pm ' +
      REGIONS[state.region].zones[state.zoneIdx][0] + '</small></span>' +
      '<div class="cov-track"><div class="cov-bar cov-bar--you" style="--start:9;--len:8">' +
      '<span class="cov-bar-label"><span>Your 9–5</span></span></div></div></div>';

    CENTERS.forEach(function (c) {
      var start, kind, label, sub;
      if (state.mode === "local") {
        /* Team works its own 9–5 local — always a day shift for them,
           mapped onto your clock. */
        start = mod24(9 + (co - c.off));
        kind = "day";
        label = "Day Shift";
        sub = "Works their 9am–5pm local &mdash; online for you " +
          fmt(start) + "–" + fmt(start + 8);
      } else {
        /* Team covers YOUR 9–5. Work out their local window and whether that
           lands in their day or night. */
        start = 9;
        var localStart = mod24(9 + (c.off - co));
        var mid = mod24(localStart + 4);
        kind = (mid >= 6 && mid < 18) ? "day" : "night";
        label = kind === "day" ? "Day Shift" : "Night Shift";
        sub = "Works your 9am–5pm &mdash; that’s " + fmt(localStart) + "–" +
          fmt(localStart + 8) + " local for them (" +
          (kind === "day" ? "a day shift" : "a night shift") + ")";
      }

      rows += '<div class="cov-row">' +
        '<span class="cov-name">' + c.name +
        ' <small>UTC' + (c.off >= 0 ? "+" : "") + c.off + '</small></span>' +
        '<div class="cov-track">' + shiftBar(start, 8, kind, label) + '</div></div>' +
        '<div class="cov-sub"><span class="cov-dot cov-dot-' + kind + '"></span> ' +
          sub + '</div>';
    });

    var scale = '<div class="cov-scale"><span>12am</span><span>6am</span><span>12pm</span><span>6pm</span><span>12am</span></div>';

    chart.innerHTML = rows + scale;

    var note = document.getElementById("cov-note");
    if (state.mode === "local") {
      note.innerHTML = "<strong>Their day shift:</strong> every center works a normal 9–5 " +
        "day shift at home. Nearshore Colombia's day overlaps yours in real time; the others' " +
        "daytime covers your evenings and overnight hours.";
    } else {
      note.innerHTML = "<strong>Your business day:</strong> each center staffs your 9am–5pm " +
        "directly. For Colombia that’s a day shift; for the Philippines, India and Kenya it’s a " +
        "night shift locally &mdash; which Cloudstaff runs as standard, fully supported.";
    }
  }

  seg("cov-mode", MODES, "mode", render);
  buildRegion();
  buildZone();
  render();
})();
