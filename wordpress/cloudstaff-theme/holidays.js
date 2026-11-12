/* Cloudstaff public holiday planner (v1.2).
   Compares the public holidays of a Cloudstaffer's service country with the
   client's own public holidays, for Monday to Friday only, and shows which
   days the team works and which days it takes off.
   The holiday data is held in the page itself, in the JSON block #hol-data. */
(function () {
  "use strict";

  var table = document.getElementById("hol-table");
  var dataEl = document.getElementById("hol-data");
  if (!table || !dataEl) return;

  var DATA = JSON.parse(dataEl.textContent);
  var YEAR = DATA.year;
  var DOW = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  var MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  var MODES = {
    client: "Take my public holidays off",
    local: "Take their local holidays off"
  };

  var state = { mode: "client", staff: "ph", country: "us", region: "fed" };

  /* --- Date helpers (dates are "MM-DD" within YEAR) ------------------------ */
  function toDate(md) {
    var p = md.split("-");
    return new Date(Date.UTC(YEAR, parseInt(p[0], 10) - 1, parseInt(p[1], 10)));
  }
  function dayNum(md) { return Math.round(toDate(md).getTime() / 86400000); }
  function isWeekend(md) { var d = toDate(md).getUTCDay(); return d === 0 || d === 6; }
  function fmt(md) {
    var d = toDate(md);
    return DOW[d.getUTCDay()] + ", " + MON[d.getUTCMonth()] + " " + d.getUTCDate();
  }
  function country(label, cap) {
    return label === "Philippines" ? (cap ? "The " : "the ") + label : label;
  }
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  /* Sort a holiday list by date and merge two holidays that share a date. */
  function tidy(list) {
    var sorted = list.slice().sort(function (a, b) { return a.d < b.d ? -1 : a.d > b.d ? 1 : 0; });
    var out = [];
    sorted.forEach(function (h) {
      var last = out[out.length - 1];
      if (last && last.d === h.d) {
        last.n += " / " + h.n;
        last.t = last.t || h.t;
        if (h.note && last.note !== h.note) last.note = last.note ? last.note + ". " + h.note : h.note;
      } else {
        out.push({ d: h.d, n: h.n, t: h.t || 0, note: h.note || "" });
      }
    });
    return out;
  }

  function staffList() { return tidy(DATA.staff[state.staff].h); }
  function clientList() {
    var c = DATA.clients[state.country];
    return tidy(c.base.concat(c.regions[state.region].h));
  }

  /* Order-preserving match between two date-sorted lists. Every holiday in the
     shorter list is paired with one in the longer list so that the total gap in
     days is as small as possible, and both columns stay in date order. A holiday
     on the same date in both lists is always paired with itself.
     Returns rows of { a: holiday|null, b: holiday|null }. */
  function align(A, B) {
    var swap = A.length > B.length;
    var S = swap ? B : A, L = swap ? A : B;
    var m = S.length, n = L.length, i, j;
    var INF = 1e12;
    function cost(si, lj) {
      var gap = Math.abs(dayNum(S[si].d) - dayNum(L[lj].d));
      return gap === 0 ? -1e6 : gap;
    }
    var dp = [];
    for (i = 0; i <= m; i++) {
      dp.push([]);
      for (j = 0; j <= n; j++) dp[i].push(i === 0 ? 0 : INF);
    }
    for (i = 1; i <= m; i++) {
      for (j = i; j <= n; j++) {
        var take = dp[i - 1][j - 1] + cost(i - 1, j - 1);
        var skip = j > i ? dp[i][j - 1] : INF;
        dp[i][j] = Math.min(take, skip);
      }
    }
    var rows = [];
    i = m; j = n;
    while (j > 0) {
      if (i > 0 && (j === i || dp[i][j] !== dp[i][j - 1])) {
        rows.push({ s: S[i - 1], l: L[j - 1] }); i--; j--;
      } else {
        rows.push({ s: null, l: L[j - 1] }); j--;
      }
    }
    rows.reverse();
    return rows.map(function (r) {
      return swap ? { a: r.l, b: r.s } : { a: r.s, b: r.l };
    });
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
      b.setAttribute("aria-pressed", state[key] === k ? "true" : "false");
      b.addEventListener("click", function () {
        state[key] = k;
        el.querySelectorAll(".tb-seg-btn").forEach(function (x) {
          x.classList.remove("is-active"); x.setAttribute("aria-pressed", "false");
        });
        b.classList.add("is-active"); b.setAttribute("aria-pressed", "true");
        onChange();
      });
      el.appendChild(b);
    });
  }

  function labels(group) {
    var o = {};
    Object.keys(group).forEach(function (k) { o[k] = group[k].label; });
    return o;
  }

  function buildRegion() {
    var c = DATA.clients[state.country];
    var sel = document.getElementById("hol-region");
    var keys = Object.keys(c.regions);
    if (!c.regions[state.region]) state.region = keys[0];
    document.getElementById("hol-region-label").textContent = c.regionLabel;
    sel.innerHTML = "";
    keys.forEach(function (k) {
      var o = document.createElement("option");
      o.value = k; o.textContent = c.regions[k].label;
      if (k === state.region) o.selected = true;
      sel.appendChild(o);
    });
    sel.disabled = keys.length < 2;
    sel.onchange = function () { state.region = sel.value; render(); };
  }

  /* --- Render -------------------------------------------------------------- */
  var SWAP = '<svg class="hol-ico" viewBox="0 0 24 24" aria-hidden="true">' +
    '<path d="M4 8h14M14 4l4 4-4 4M20 16H6M10 12l-4 4 4 4"/></svg>';
  var SAME = '<svg class="hol-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9h12M6 15h12"/></svg>';

  function flag(code, name) {
    return '<img class="flag" src="https://flagcdn.com/' + code + '.svg" width="24" height="18" alt="' +
      esc(name) + '" loading="lazy" decoding="async">';
  }

  function cell(h, kind) {
    if (!h) return "";
    return '<div class="hol-cell hol-cell--' + kind + '">' +
      '<span class="hol-date">' + fmt(h.d) + '</span>' +
      '<span class="hol-name">' + esc(h.n) + '</span>' +
      (h.t ? '<span class="hol-tag">Date to be confirmed</span>' : '') +
      (h.note ? '<span class="hol-cell-note">' + esc(h.note) + '</span>' : '') +
      '</div>';
  }
  function empty(text) { return '<div class="hol-cell hol-cell--empty">' + text + '</div>'; }

  /* Placeholder that keeps a one-sided row in its own column. */
  var BLANK = '<div class="hol-cell hol-cell--blank" aria-hidden="true"></div>';

  function row(left, mid, right, cls) {
    return '<div class="hol-row' + (cls ? " " + cls : "") + '">' + left +
      '<div class="hol-mid">' + mid + '</div>' + right + '</div>';
  }

  function tile(value, label) {
    return '<div class="hol-tile"><span class="hol-tile-value">' + value +
      '</span><span class="hol-tile-label">' + label + '</span></div>';
  }

  function render() {
    var s = DATA.staff[state.staff];
    var c = DATA.clients[state.country];
    var regionName = c.regions[state.region].label;
    var all = { a: staffList(), b: clientList() };
    var wk = function (h) { return !isWeekend(h.d); };
    var we = function (h) { return isWeekend(h.d); };
    var A = all.a.filter(wk), B = all.b.filter(wk);
    var rows = align(A, B);
    var swapMode = state.mode === "client";

    var same = 0, paired = 0, onlyA = 0, onlyB = 0, html = "";
    var workKind = "work", offKind = "off";

    html += '<div class="hol-head">' +
      '<div class="hol-head-col">' +
        '<span class="hol-head-title">' + (swapMode ? "Staff will work these days" : "Staff will take these days off") + '</span>' +
        '<span class="hol-head-sub">' + flag(s.flag, s.label) + ' ' + esc(s.long || s.label) + ' public holidays</span></div>' +
      '<div class="hol-mid"></div>' +
      '<div class="hol-head-col">' +
        '<span class="hol-head-title">' + (swapMode ? "Staff will take these days off" : "Staff will work these days") + '</span>' +
        '<span class="hol-head-sub">' + flag(c.flag, c.label) + ' Your public holidays, ' + esc(regionName) + '</span></div>' +
      '</div>';

    if (swapMode) {
      rows.forEach(function (r) {
        if (r.a && r.b && r.a.d === r.b.d) {
          same++;
          var names = r.a.n === r.b.n ? r.a.n : r.a.n + " / " + r.b.n;
          html += '<div class="hol-row hol-row--same"><div class="hol-cell hol-cell--same">' +
            '<span class="hol-date">' + fmt(r.a.d) + '</span>' +
            '<span class="hol-name">' + esc(names) + '</span>' +
            '<span class="hol-cell-note">Public holiday in both places. Your team is off and nothing needs to be swapped.</span>' +
            '</div></div>';
        } else if (r.a && r.b) {
          paired++;
          html += row(cell(r.a, workKind), SWAP, cell(r.b, offKind));
        } else if (r.a) {
          onlyA++;
          html += row(cell(r.a, workKind), "", empty("No public holiday of yours left to swap with"), "hol-row--open");
        } else {
          onlyB++;
          html += row(empty("No local public holiday left to swap with"), "", cell(r.b, offKind), "hol-row--open");
        }
      });
    } else {
      /* Team follows its own calendar: a plain date-ordered list, no pairing. */
      var seen = {}, events = [];
      A.forEach(function (h) { seen[h.d] = { a: h, b: null }; events.push(seen[h.d]); });
      B.forEach(function (h) {
        if (seen[h.d]) seen[h.d].b = h; else events.push({ a: null, b: h });
      });
      events.sort(function (x, y) {
        var dx = (x.a || x.b).d, dy = (y.a || y.b).d;
        return dx < dy ? -1 : dx > dy ? 1 : 0;
      });
      events.forEach(function (r) {
        if (r.a && r.b) {
          same++;
          var names = r.a.n === r.b.n ? r.a.n : r.a.n + " / " + r.b.n;
          html += '<div class="hol-row hol-row--same"><div class="hol-cell hol-cell--same">' +
            '<span class="hol-date">' + fmt(r.a.d) + '</span>' +
            '<span class="hol-name">' + esc(names) + '</span>' +
            '<span class="hol-cell-note">Public holiday in both places. Your team is off and so are you.</span>' +
            '</div></div>';
        } else if (r.a) {
          onlyA++;
          html += row(cell(r.a, offKind), "", BLANK);
        } else {
          onlyB++;
          html += row(BLANK, "", cell(r.b, workKind));
        }
      });
    }

    /* Weekend holidays, listed for completeness. */
    var wa = all.a.filter(we), wb = all.b.filter(we);
    if (wa.length || wb.length) {
      var list = function (hs) {
        if (!hs.length) return '<p class="hol-weekend-none">None in ' + YEAR + '</p>';
        return '<ul class="hol-weekend-list">' + hs.map(function (h) {
          return '<li><span class="hol-date">' + fmt(h.d) + '</span> ' + esc(h.n) +
            (h.t ? ' <span class="hol-tag">Date to be confirmed</span>' : '') + '</li>';
        }).join("") + '</ul>';
      };
      html += '<div class="hol-weekend"><span class="hol-weekend-title">Public holidays that fall on a weekend</span>' +
        '<span class="hol-weekend-sub">Listed for completeness. A Monday to Friday team is not working on these days, so nothing changes.</span>' +
        '<div class="hol-weekend-cols"><div><span class="hol-head-sub">' + flag(s.flag, s.label) + ' ' + esc(s.long || s.label) + '</span>' + list(wa) + '</div>' +
        '<div><span class="hol-head-sub">' + flag(c.flag, c.label) + ' ' + esc(c.label) + ', ' + esc(regionName) + '</span>' + list(wb) + '</div></div></div>';
    }

    table.innerHTML = html;

    var tiles = document.getElementById("hol-tiles");
    if (swapMode) {
      tiles.innerHTML =
        tile(A.length, esc(s.label) + " public holidays, Monday to Friday") +
        tile(B.length, "Your public holidays, Monday to Friday") +
        tile(same, "Fall on the same day") +
        tile(paired, "Swapped one for one") +
        tile(onlyA + onlyB, onlyB ? "Of your holidays left without a swap" : "Local holidays left without a swap");
    } else {
      tiles.innerHTML =
        tile(A.length, esc(s.label) + " public holidays, Monday to Friday") +
        tile(B.length, "Your public holidays, Monday to Friday") +
        tile(same, "Fall on the same day") +
        tile(onlyA, "Days your team is off while you are open") +
        tile(onlyB, "Days your team works while you are closed");
    }

    var note = document.getElementById("hol-note");
    var text;
    if (swapMode) {
      text = "<strong>Take my public holidays off:</strong> your team works through its local public holidays " +
        "and takes yours instead. Each local holiday is paired with the closest holiday of yours that is still free, in date order. ";
      if (onlyA) text += esc(country(s.label, true)) + " has more weekday public holidays than you do in " + YEAR +
        ", so " + onlyA + " cannot be swapped. Agree with your Cloudstaff Account Manager how those days are treated. ";
      if (onlyB) text += "You have more weekday public holidays than " + esc(country(s.label, false)) + " does in " + YEAR +
        ", so " + onlyB + " of yours " + (onlyB === 1 ? "has" : "have") + " no local holiday to swap with. Agree with your Cloudstaff Account Manager how those days are treated. ";
    } else {
      text = "<strong>Take their local holidays off:</strong> your team follows its own public holiday calendar. " +
        "The left column shows the days it is off, and the right column shows your public holidays, when it keeps working. ";
    }
    text += "Dates are for " + YEAR + ". Sources: " + esc(s.source) + "; " + esc(c.source) +
      ". Holidays marked “Date to be confirmed” can move. Planner v" + esc(DATA.version) + ".";
    note.innerHTML = text;
  }

  seg("hol-mode", MODES, "mode", render);
  seg("hol-staff", labels(DATA.staff), "staff", render);
  seg("hol-country", labels(DATA.clients), "country", function () {
    state.region = Object.keys(DATA.clients[state.country].regions)[0];
    buildRegion();
    render();
  });
  buildRegion();
  render();
})();
