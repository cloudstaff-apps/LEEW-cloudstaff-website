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

  function barHtml(start, len, cls) {
    return segs(start, len).map(function (s) {
      return '<div class="cov-bar ' + cls + '" style="--start:' + s.start +
        ';--len:' + s.len + '"></div>';
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
      '<div class="cov-track">' + barHtml(9, 8, "cov-bar-you") + '</div></div>';

    CENTERS.forEach(function (c) {
      /* Day shift: center 9-17 local, shown on client clock */
      var dayStart = mod24(9 + (co - c.off));
      /* Aligned shift: center works client 9-17 -> on client clock that's 9-17;
         compute the center's LOCAL window for the label */
      var alignLocalStart = mod24(9 + (c.off - co));
      var dayActive = state.mode === "local";
      var dayLocal = "their 9am–5pm";
      var alignLocal = fmt(alignLocalStart) + "–" + fmt(alignLocalStart + 8) + " local";

      rows += '<div class="cov-row">' +
        '<span class="cov-name">' + c.flag + ' ' + c.name +
        ' <small>UTC' + (c.off >= 0 ? "+" : "") + c.off + '</small></span>' +
        '<div class="cov-track">' +
          barHtml(dayStart, 8, "cov-bar-day" + (dayActive ? " is-active" : "")) +
          barHtml(9, 8, "cov-bar-align" + (!dayActive ? " is-active" : "")) +
        '</div></div>' +
        '<div class="cov-sub">' +
          (dayActive
            ? '<span class="cov-dot cov-dot-day"></span> Works ' + dayLocal +
              ' &mdash; online for you ' + fmt(dayStart) + '–' + fmt(dayStart + 8)
            : '<span class="cov-dot cov-dot-align"></span> Works your 9am–5pm &mdash; that’s ' +
              alignLocal + ' for them') +
        '</div>';
    });

    var scale = '<div class="cov-scale"><span>12am</span><span>6am</span><span>12pm</span><span>6pm</span><span>12am</span></div>';

    chart.innerHTML = rows + scale;

    var note = document.getElementById("cov-note");
    if (state.mode === "local") {
      note.innerHTML = "<strong>Their day shift:</strong> each center works its own 9–5. " +
        "Nearshore Colombia overlaps your day in real time; the Philippines and India run your " +
        "overnight hours; Kenya covers your morning. Hover the bars to read local times.";
    } else {
      note.innerHTML = "<strong>Your business day:</strong> each center staffs your 9–5 directly. " +
        "For Colombia that’s a normal day shift; for the Philippines, India and Kenya it means an " +
        "evening or night shift locally &mdash; which Cloudstaff runs as standard, fully supported.";
    }
  }

  seg("cov-mode", MODES, "mode", render);
  buildRegion();
  buildZone();
  render();
})();
