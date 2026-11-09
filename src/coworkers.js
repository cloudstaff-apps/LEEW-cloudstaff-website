/* Cloudstaff AI Coworker directory — Cloudstaff's own live Coworkers, grouped
   by business function with a category filter. Read-only; data embedded. */
(function () {
  "use strict";
  var root = document.getElementById("cw-directory");
  if (!root) return;

  var ORDER = ["Sales", "Technology", "Facilities", "HR", "Operations",
    "Communications", "Relationships", "Supply chain", "Finance",
    "Marketing", "Reception"];

  var DATA = [
    { c: "Sales", n: "Emma Frost", u: "Crmboss", d: "Keeps sales managers on top of pipeline activity in HubSpot and flags when targets slip.", t: ["HubSpot", "KPIs"] },
    { c: "Sales", n: "Helen Foster", u: "TheHunt", d: "Runs the sales CRM day to day: clean records, reminders, and the reports managers need.", t: ["CRM", "Sales management"] },

    { c: "Technology", n: "Clive Spencer", u: "Sparkboss", d: "Finds the next AI Coworkers to build and turns each idea into a job description.", t: ["AI adoption", "Process discovery"] },
    { c: "Technology", n: "David Lewis", u: "AlphaBoss", d: "The admin platform that monitors every Coworker unit and manages incidents.", t: ["IT operations", "Monitoring"] },
    { c: "Technology", n: "Dylan Owen", u: "TheBoss", d: "The reference server every Coworker unit is built from: sign-in, library, security.", t: ["Reference server", "Unit framework"] },
    { c: "Technology", n: "Thomas Jackson", u: "Bruceboss", d: "The reference unit that proves the shared design system for every Coworker.", t: ["Design system", "Reference server"] },

    { c: "Facilities", n: "Carla Hewitt", u: "Labelboss", d: "Watches every office label printer and designs and prints labels on demand.", t: ["Printer monitoring", "Labels"] },
    { c: "Facilities", n: "Edgar Bailey", u: "Lockerboss", d: "Assigns lockers and tracks every key, with each change recorded.", t: ["Lockers", "Key tracking"] },
    { c: "Facilities", n: "Leah Webb", u: "Roomboss", d: "Finds and books meeting rooms by size and equipment, and reminds approvers.", t: ["Room booking", "Meetings"] },
    { c: "Facilities", n: "Rebecca Ellis", u: "Keyboss", d: "Tracks physical keys and who holds them, so a missing key can be traced.", t: ["Physical keys", "Key handovers"] },
    { c: "Facilities", n: "Rosie Smith", u: "Fleetboss", d: "Manages the vehicle fleet: requests, approvals, bookings, and mileage.", t: ["Vehicle fleet", "Vehicle bookings"] },
    { c: "Facilities", n: "Sean Day", u: "Courierboss", d: "Tracks internal deliveries between offices, scanned at every hand-over.", t: ["Internal deliveries", "Package tracking"] },
    { c: "Facilities", n: "Stephen Sullivan", u: "Lostfoundboss", d: "Gets lost property back to its owner, checking every claim.", t: ["Lost property", "Claims"] },

    { c: "HR", n: "Alice Dalton", u: "Leaveboss", d: "Runs leave and absence across six countries and keeps approvals moving.", t: ["Leave management", "Approvals"] },
    { c: "HR", n: "Annabel Jones", u: "Swagboss", d: "The staff store: branded merchandise ordered and paid through payroll.", t: ["Staff store", "Merchandise"] },
    { c: "HR", n: "Jamie Frost", u: "SirBoss", d: "A training simulator that gives new starters realistic practice with feedback.", t: ["Training", "Simulation"] },
    { c: "HR", n: "Mike West", u: "Open-Mic", d: "The HR reporting system: regular reports, pulse scores, KPIs and scorecards.", t: ["Staff reporting", "KPIs"] },

    { c: "Operations", n: "Julie White", u: "Travelboss", d: "Plans and books staff travel, with approvals and tickets on the traveller's phone.", t: ["Travel", "Trip planning"] },
    { c: "Operations", n: "Lisa Ward", u: "EventBoss", d: "Runs events end to end: QR tickets, check-in, and attendance reporting.", t: ["Events", "Ticketing"] },
    { c: "Operations", n: "Luke Riley", u: "Taskboss", d: "The executive team's task system: a daily plate for each person, chasing overdue work.", t: ["Executive support", "Task management"] },
    { c: "Operations", n: "Scott Parks", u: "ProcessBox", d: "The process library: walks staff through approved steps and keeps them reviewed.", t: ["Process library", "Documentation"] },
    { c: "Operations", n: "Simon Hunt", u: "Standupboss", d: "Runs the daily standup: collects updates, presents the deck, reports blockers.", t: ["Daily standups", "Meetings"] },

    { c: "Communications", n: "Adam Ross", u: "Noteboss", d: "Curates what's worth sharing, tags it, and sends digests to the right people.", t: ["Knowledge", "Content curation"] },
    { c: "Communications", n: "Joel Kane", u: "Infoboss", d: "Researches topics the business cares about and circulates what's worth reading.", t: ["Research", "News curation"] },
    { c: "Communications", n: "Oscar Cook", u: "Newsboss", d: "The internal newsroom: clear articles sent to the right people across every channel.", t: ["Internal news", "Newsletters"] },
    { c: "Communications", n: "William Coleman", u: "Oneroom", d: "Puts the switchboard on one screen for one-click video calls, with health reporting.", t: ["Video calls", "Switchboard"] },

    { c: "Relationships", n: "Craig Baxter", u: "ApacYoga", d: "Trust relationship management for the APAC team: records, promises, morning priorities.", t: ["Trust management", "APAC"] },
    { c: "Relationships", n: "Laura Jones", u: "Cloudstaff.Yoga", d: "The trust relationship system: one record per contact, and briefs you before meetings.", t: ["Trust management", "Meeting briefs"] },
    { c: "Relationships", n: "Sadie Clarke", u: "Try Yoga", d: "A trial instance of the Yoga trust system to try before rolling it out.", t: ["Trust management", "Product trial"] },
    { c: "Relationships", n: "Sarah Reid", u: "Optiboss", d: "Trust relationship management: keeps promises on track and briefs you before meetings.", t: ["Trust management", "Meeting briefs"] },

    { c: "Supply chain", n: "Elliot Payne", u: "Returnboss", d: "Runs supplier returns, damage claims and credit notes under your rules.", t: ["Returns", "Credit notes"] },
    { c: "Supply chain", n: "Henry Godfrey", u: "Freightboss", d: "Runs the freight desk: quotes, bookings, shipment tracking and bill checks.", t: ["Freight", "Shipment tracking"] },
    { c: "Supply chain", n: "Howard Booth", u: "Vendorboss", d: "Onboards and manages suppliers: certificates, contracts, approvals and scorecards.", t: ["Supplier management", "Supplier compliance"] },
    { c: "Supply chain", n: "Louis Reid", u: "Purchaseboss", d: "Runs purchasing: approvals under your rules, chased, and posted to the ERP.", t: ["Procurement", "Purchase orders"] },

    { c: "Finance", n: "Chris Hayes", u: "ExpenseBoss", d: "The expense system: reads receipts, chases approvals, and readies a trusted payment run.", t: ["Expense claims", "Approvals"] },
    { c: "Finance", n: "Melissa Nelson", u: "Collectionboss", d: "Chases overdue invoices: drafts reminders from templates for a person to approve.", t: ["Collections", "Accounts receivable"] },

    { c: "Marketing", n: "Josephine Allen", u: "Storyboss", d: "Collects employee stories and case studies for marketing.", t: ["Employee stories", "Case studies"] },

    { c: "Reception", n: "Claire West", u: "Visitorboss", d: "The visitor check-in system: pre-registration, QR passes, badges, and arrival alerts.", t: ["Visitor management", "Badges"] },
    { c: "Reception", n: "Jane Doyle", u: "Front Desk", d: "The remote receptionist: visitors reach a live switchboard by audio, video and chat.", t: ["Remote receptionist", "Video calls"] }
  ];

  var state = { cat: "All" };

  function initials(name) {
    return name.replace(/[^A-Za-z ]/g, "").split(/\s+/).filter(Boolean)
      .map(function (w) { return w[0]; }).slice(0, 2).join("").toUpperCase();
  }

  function card(x) {
    return '<article class="card cw-card">' +
      '<div class="cw-head"><span class="avatar-initials">' + initials(x.n) + '</span>' +
      '<span class="cw-id"><strong class="cw-name">' + x.n + '</strong>' +
      '<span class="cw-unit">' + x.u + '</span></span></div>' +
      '<p class="cw-desc">' + x.d + '</p>' +
      '<ul class="cs-results">' + x.t.map(function (t) { return '<li>' + t + '</li>'; }).join("") + '</ul>' +
      '<span class="cw-cat-tag">' + x.c + '</span></article>';
  }

  function render() {
    var list = DATA.filter(function (x) { return state.cat === "All" || x.c === state.cat; });
    root.querySelector(".cw-grid").innerHTML = list.map(card).join("");
  }

  var chips = ["All"].concat(ORDER);
  root.innerHTML =
    '<div class="cw-filter" role="group" aria-label="Filter by function">' +
    chips.map(function (c) {
      var count = c === "All" ? DATA.length : DATA.filter(function (x) { return x.c === c; }).length;
      return '<button type="button" class="cw-chip' + (c === "All" ? " is-active" : "") +
        '" data-cat="' + c + '">' + c + ' <span class="cw-count">' + count + '</span></button>';
    }).join("") +
    '</div><div class="cw-grid grid-3"></div>';

  root.querySelectorAll(".cw-chip").forEach(function (b) {
    b.addEventListener("click", function () {
      state.cat = b.getAttribute("data-cat");
      root.querySelectorAll(".cw-chip").forEach(function (x) { x.classList.remove("is-active"); });
      b.classList.add("is-active");
      render();
    });
  });

  render();
})();
