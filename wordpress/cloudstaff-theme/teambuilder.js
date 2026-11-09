/* Cloudstaff Team Builder, proof of concept.
   All pricing is PLACEHOLDER data for demonstration only.
   Role catalog sourced from the Cloudstaff CFO Kit (July 2026). */
(function () {
  "use strict";

  /* ------------------------------------------------------------------ */
  /* Role catalog: category -> roles                                     */
  /* ------------------------------------------------------------------ */
  var CATALOG = {
    "Accounting & Finance": ["Accountant (General)", "Accounting Assistant", "Accounting Associate", "Accounting Clerk", "Accounting Manager", "Accounting Officer", "Accounting Support Agent", "Accounting Technician", "Accounting, Payroll & HR Coordinator", "Accounts Officer", "Accounts Payable Manager", "Accounts Payable Officer", "Accounts Receivable Manager", "Accounts Receivable Officer", "Associate Accountant", "Audit & Assurance Officer", "Audit Assistant", "Billing Operations Analyst", "Bookkeeper", "Corporate Accountant", "Cost Accountant", "Finance Director", "Finance Manager", "Financial Accountant", "Financial Controller", "Financial Planning & Analysis Manager", "FP&A Analyst", "Fund Accountant", "Insolvency Analyst", "Inventory Accountant", "Invoicing Assistant", "Lead Reconciliation Specialist", "Management Accountant", "MYOB Accountant", "Payment Processor", "Payroll Assistant", "Payroll Manager", "Property Management Accountant", "QuickBooks Accountant", "Revenue Accountant", "Risk Management Associate", "Sage 50 Accountant", "SMSF Accountant", "Tax Accountant", "Tax Manager", "Transaction Advisory Associate", "Treasury Accountant", "Treasury Officer", "Trust Accounting Specialist", "Xero Accountant"],
    "Administration, VA & Executive Support": ["Admin Assistant", "Admin Manager", "Back Office Administrator", "Back Office Specialist", "Business Information Specialist", "Client Information Specialist", "Client Operations Assistant", "Customer Operations Manager", "Data Entry Lead", "Data Entry Specialist", "Evaluation Specialist", "Executive Administrative Assistant", "Executive Assistant", "Executive Services Manager", "Franchising Administration Coordinator", "Invoice Processing Specialist", "Licensing Coordinator", "Operations Administration Specialist", "Order Processing Specialist", "Payments Lead", "Personal Assistant", "Research Specialist", "Senior Administrative Coordinator", "Senior Client Information Specialist", "Senior Customer Coordinator", "Team Leader for Receptionists", "Technical Assistant", "Transcription Specialist", "Virtual Assistant"],
    "Architecture & Design": ["Architect", "Commercial Architect", "Industrial Designer", "Interior Designer", "Landscape Designer", "Residential Architect", "Senior Architect", "Urban Designer & Planner"],
    "Artificial Intelligence": ["AI Algorithm Developer", "AI Business Development Manager", "AI Data Annotator", "AI Ethics & Policy Expert", "AI Governance & Safety Officer", "AI Model Risk Analyst", "AI Product Manager", "AI Prompt Engineer", "AI Trainer & Data Curator", "AI UX Designer", "NLP Engineer"],
    "Banking & Financial Services": ["Assistant Underwriter", "Broker Assistant", "Broker Support & Credit Analyst", "Customer Analyst Team Leader", "Customer Insights Analyst", "Financial Management Specialist", "Financial Planning Assistant", "Inbound Settlement Operations Manager", "Investment Management Specialist", "Loan Assessment Consultant", "Loan Packaging Assistant", "Loan Processor", "Paraplanner", "Safety & Claims Officer", "Senior Financial Planning Assistant", "Senior Paraplanner", "Underwriting Assistant"],
    "Business Analysis & Product": ["Business Analyst", "Implementation Consultant", "Product Director", "Product Manager", "Product Owner"],
    "Cloud & Infrastructure": ["Associate Cloud Operations Engineer", "Cloud Applications Engineer", "Cloud Engineer", "Cloud Migration Engineer", "Infrastructure Architect"],
    "Collections & Credit Control": ["Collections Agent", "Collections Manager", "Credit Manager", "Debt Collector"],
    "Construction & Estimating": ["Estimating Manager", "Estimator", "Mechanical Estimator", "Quantity Surveyor", "Structural Estimator"],
    "Creative & Multimedia": ["3D Artist & Renderer", "3D Modeller & CAD Designer", "Animator", "Assistant Producer", "Associate Graphic Designer", "Associate Multimedia Specialist", "Creative Specialist", "Digital Artist", "Director of Photography", "Graphic Design Team Leader", "Graphic Designer", "Head Writer", "Motion Graphics Designer", "Multimedia Specialist", "Photo Editor", "Prepress & Workflow Operator", "Print Graphic Designer", "Producer", "Production Team Leader", "Scriptwriter", "Video Editor", "Videographer", "Voice Artist", "Web Designer"],
    "Customer Service & Contact Centre": ["Call Centre Agent", "Call Quality Analyst", "Chat Support Agent", "Client Care Team Leader", "Contact Centre Associate", "Contact Centre Trainer", "Customer Care Representative", "Customer Case Manager", "Customer Service Analyst", "Customer Service Manager", "Customer Service Representative", "Customer Service Team Leader", "Customer Support Specialist", "Customer Technical Support Specialist", "Data & Quality Manager", "Digital Support Team Leader", "Email Support Agent", "Quality Assurance Officer", "Senior Customer Service Agent", "Support Team Manager", "Voice Agent"],
    "Customer Success": ["Account Management Assistant", "Client Experience Manager", "Client Relationship Manager", "Client Services Manager", "Customer Liaison Officer", "Customer Success Manager", "Customer Success Operations Associate", "Group Leader of Customer Success", "Head of Customer Success", "Membership Renewals Specialist", "VP of Customer Success"],
    "Cybersecurity": ["Associate Qualified Security Assessor", "Cloud Security Specialist", "Continuous Compliance Management Associate", "Continuous Compliance Management Team Manager", "DevSecOps Specialist", "Hardware Security Specialist", "Offensive Security Manager", "Password Management Specialist", "Penetration Tester", "Qualified Security Assessor", "Security Analyst", "Software Security Specialist"],
    "Data & Analytics": ["Business Intelligence Consultant", "Data & Reporting Analyst", "Data Scientist", "Reporting Analyst"],
    "E-commerce": ["Amazon Product Sourcer", "Amazon Specialist", "Amazon Store Manager", "Content QA Editor", "Drop Shipping Specialist", "E-commerce Analyst", "E-commerce Assistant", "E-commerce Marketing Specialist", "E-commerce Operations Specialist", "E-commerce Order Processor", "E-commerce Team Leader", "E-commerce Virtual Assistant", "eBay Specialist", "Marketplace Operations Officer", "Marketplace Store Specialist", "Product Classification Specialist", "Product Data Sourcing Specialist", "Product Data Specialist", "Product Listing Specialist", "Product Sourcing Specialist", "Shopify Administrator"],
    "Electronics & Embedded Systems": ["Electronics Engineer", "Embedded Hardware Engineer", "Embedded Software Engineer", "Firmware Engineer", "Power Design Engineer"],
    "Engineering": ["Aerospace Electrical Engineer", "BIM Modeler", "Civil Engineer", "Design Engineer", "Drafting Designer", "Drafting & Engineering Assistant", "Electrical Control Engineer", "Electrical Design Engineer", "Electrical Distribution Designer", "Electrical Project Engineer", "Engineer", "Engineering Drafting Manager", "HVAC Specialist", "Lighting Designer", "Mechanical Design Drafter", "Mechanical Engineer", "P&ID Specialist", "Piping & Pump Systems Specialist", "Principal Electrical Engineer", "Process Engineer", "Product Engineer", "Structural Designer"],
    "Events & Experiences": ["Event AV Technician", "Event Coordinator", "Event Manager", "Event Production Manager", "Event Technical & Logistics Assistant", "Event Visual Coordinator", "Hospitality Coordinator", "Venue Coordinator"],
    "Executive Leadership": ["Chief Channel Officer", "Chief Compliance Officer", "Chief Executive Officer", "Chief Financial Officer", "Chief Human Resources Officer", "Chief Product Officer", "Chief Sales & Marketing Officer", "Chief Technology Officer"],
    "Facilities & Workplace Services": ["Facilities Manager", "Facilities Officer", "Facilities Site Administration Officer", "Facilities Supervisor", "Office Lease Manager", "Office Lease Officer", "OH&S Manager", "Security Consultant", "Senior Office Lease Manager", "Senior Site Manager", "Site Manager", "Transport Coordinator"],
    "Healthcare Support": ["Clinic Operations Manager", "Healthcare Client Services Specialist", "Healthcare Project Support Officer", "Medical Coder"],
    "Human Resources": ["Assistant HR Manager", "Director of Staff Relations", "HR & Administration Assistant", "HR & Administration Officer", "HR & Talent Officer", "HR Assistant", "HR Business Partner", "HR Director", "HR Generalist", "HR Manager", "HR Manager, Systems & Reports", "HR Officer", "HR Supervisor", "HR Team Leader", "Labour Relations Manager", "Staff Relations Assistant", "Staff Relations Generalist", "Staff Relations Manager", "Staff Relations Officer"],
    "IT Support & Networks": ["Assistant Service Manager", "Associate Support Specialist", "Configuration SME Team Leader", "Database Administrator", "Firewall Support Specialist", "Hub System Support", "IT Helpdesk Manager", "IT Helpdesk Specialist", "IT Manager", "IT Technical Manager", "Linux Administrator", "Network Administrator", "Network Engineer", "Network Operations Engineer", "Network Operations Manager", "Production Support Specialist", "Provisioning & Accounts Coordinator", "Provisioning & Porting Coordinator", "Provisioning & Porting Senior Coordinator", "Provisioning & Porting Team Leader", "Senior Service Desk Analyst", "Server Administrator", "Software Support Representative", "Solutions Architect", "Support Analyst", "Technical Support", "Technical Support Manager", "Technical Support Specialist", "VoIP Specialist", "Windows Administrator"],
    "Learning, Development & Training": ["Accounting Trainer", "Accounting Training Manager", "Learning & Development Specialist", "Senior Learning & Development Coordinator", "Training Coordinator", "Training Manager", "Training Officer"],
    "Legal & Compliance": ["Case Manager", "Compliance Specialist", "Contract Administrator", "Conveyancing Account Manager", "Director of Legal Affairs", "Document Coder", "Document Processing Specialist", "Document Reviewer", "Legal Administrative Assistant", "Legal Administrator", "Legal Analyst", "Legal Appointment Setter", "Legal Assistant", "Legal Billing Clerk", "Legal Collections Specialist", "Legal Document Reviewer", "Legal Executive Assistant", "Legal Intake Assistant", "Legal Records Manager", "Legal Researcher", "Legal Secretary", "Legal Support Specialist", "Legal Transcription Specialist", "Litigation Support Specialist", "Manager of Legal Affairs", "Paralegal", "Patent & Intellectual Property Specialist", "Records Clerk"],
    "Logistics & Supply Chain": ["3PL Specialist", "Control State Inventory Manager", "Demand Planning Manager", "E-commerce Logistics Specialist", "Expediting Specialist", "Logistics & Shipping Coordinator", "Logistics & Supply Chain Specialist", "Logistics Analyst", "Logistics Manager", "Order Fulfilment Specialist", "Procurement Manager", "Procurement Officer", "Production & Planning Specialist", "Purchasing Associate", "Sourcing Specialist", "Supply Chain Manager", "Supply Chain Support Specialist", "Supply Management Officer"],
    "Marketing & Content": ["Affiliate Marketing Specialist", "Brand Manager", "Business Writer", "Campaign Planner", "Client Success Campaign Coordinator", "Communications Manager", "Content Curator Specialist", "Content Writer", "Copywriter", "Creative Writer", "Digital Marketing Manager", "Director of Demand Generation", "Editor & Proofreader", "Ghostwriter", "Google Ads Specialist", "Grant Writer", "Head of Content & Communications", "HubSpot Administrator", "Instructional Designer", "Link Builder", "LinkedIn Advertising Specialist", "Market Research Associate", "Marketing Assistant", "Marketing Associate", "Marketing Consultant", "Marketing Coordinator", "Marketing Operations Manager", "Marketing Team Leader", "Product Marketing Manager", "Regional Demand Generation Manager", "Regional Demand Generation Specialist", "SEM Specialist", "SEO Specialist", "SEO Writer", "Social Media Manager", "Social Media Marketer", "Technical Writer", "Tutorial Writer", "VP of Brand", "VP of Demand Generation & Sales", "VP of Marketing", "VP of Marketing Operations", "VP of Product Marketing", "Web Content & Article Writer"],
    "Project Management & Operations": ["Business Planner", "Data Services Manager", "Operations Manager", "Operations Officer", "Operations Team Leader", "PMO Analyst", "Process Excellence Manager", "Project Administration Officer", "Project Coordinator", "Project Manager", "Project Support Officer", "Returns Operations Officer", "Scrum Master", "Senior Operations Analyst", "Senior Project Manager", "Service Delivery Manager", "Team Manager"],
    "Quality & Management Systems": ["IMS Admin Assistant", "IMS Audit Manager", "IMS Manager", "IMS Specialist", "ISO Consultant", "Senior IMS Manager"],
    "Real Estate & Property Services": ["Bookings Operator", "General Manager, Property Services", "Head of Go-to-Market, Property Services", "Leasing Support", "Property Management Assistant", "Property Management Support", "Property Services Team Leader", "Real Estate Accounts Assistant", "Real Estate Administration Manager", "Real Estate Applications Specialist", "Real Estate Arrears & Invoicing Specialist", "Real Estate Client Services Specialist", "Real Estate Contract Reviewer", "Real Estate Contracts Administrator", "Real Estate Database Administrator", "Real Estate Inspections Specialist", "Real Estate Listings Specialist", "Real Estate Maintenance Specialist", "Real Estate Marketing Specialist", "Real Estate New Business Support", "Real Estate Receptionist", "Real Estate Renewals Specialist", "Real Estate Sales & New Business Support", "Real Estate Sales & PM Administrator", "Real Estate Sales Virtual Assistant", "Real Estate Trainer", "Relationship & Asset Manager Associate", "Rental Trust Accountant", "Rentals Assistant", "Trust Accounting Team Leader"],
    "Recruitment & Talent Acquisition": ["Chief Recruitment Officer", "Recruitment Assistant", "Recruitment Manager", "Recruitment Marketing Specialist", "Recruitment Specialist", "Recruitment Supervisor", "Recruitment Team Leader", "Talent Acquisition Manager", "Talent Acquisition Specialist", "Technology Talent Acquisition Manager"],
    "Sales & Business Development": ["Account Director", "Account Manager", "Appointment Setter", "Associate Account Manager", "Business Development Administrator", "Business Development Analyst", "Business Development Manager", "Corporate Sales Manager", "Country Manager", "Director of Partnerships", "Director of Sales", "Head of Business Development", "Head of Sales", "Inbound Sales Specialist", "Independent Sales Consultant", "Inside Sales Agent", "Lead Administrator", "Lead Generation Program Manager", "Lead Generation Specialist", "Lead Generation Team Lead", "Outbound Calling Specialist", "Outbound Sales Specialist", "Outbound Sales Supervisor", "Sales & Marketing Assistant", "Sales & Marketing Manager", "Sales Administration Assistant", "Sales Administrator", "Sales Assistant", "Sales Associate", "Sales Development Representative", "Sales Lab Director", "Sales Manager", "Sales Operations Manager", "Sales Personal Assistant", "Sales Subject Matter Expert", "Sales Support Specialist", "Sales Team Manager", "Senior Sales Executive", "Team Growth Manager", "Telemarketer", "Telemarketing Supervisor", "Telesales Specialist", "VP of Growth", "VP of Partnerships", "VP of Sales"],
    "Software Development": [".NET Developer", "3D Modeling Developer", "Acumatica Developer", "Android Developer", "Angular Developer", "ASP Developer", "Associate Software Engineer", "Azure Developer", "Back-End Developer", "BI Developer", "Blockchain Developer", "C# Developer", "Configuration Analyst", "Configuration Team Leader", "CPQ Developer", "CRM Developer", "CSS Developer", "Dart Developer", "Developer", "Development Service Delivery Consultant", "Drupal Developer", "Dynamics Developer", "E-commerce Developer", "ERP Developer", "Flutter Developer", "Front-End Developer", "Front-End Development Manager", "Full-Stack Developer", "GIS Developer", "Golang Developer", "GSS Developer", "HTML Developer", "IBM BPM Developer", "iOS Developer", "IT Consultant", "Java Developer", "JavaScript Developer", "Joomla Developer", "Klipfolio Developer", "LAMP Developer", "Laravel Developer", "Magento Developer", "Microsoft 365 Developer", "Microsoft Dynamics 365 Developer", "Microsoft Dynamics Developer", "Mobile Developer", "MongoDB Developer", "MuleSoft Developer", "MYOB Developer", "NetSuite Developer", "Node.js Developer", "Oracle Developer", "Perl Developer", "PHP Developer", "PHP/LAMP Developer", "Power BI Developer", "Principal Developer", "Python Developer", "R Developer", "React Developer", "Release Manager", "Ruby on Rails Developer", "Rust Developer", "Salesforce Administrator", "Salesforce Consultant", "Salesforce Developer", "SAP Developer", "SAS Developer", "ServiceNow Developer", "Shopify Developer", "Software Engineer", "Spring Developer", "SQL Developer", "SSAS Developer", "SSIS Developer", "UiPath Developer", "Unity Developer", "Unreal Developer", "UX/UI Specialist", "Web Developer", "WordPress Developer", "Xamarin Developer", "Zoho Developer"],
    "Software Testing & QA": ["Associate Software QA Engineer", "Automation Tester", "Manual Tester", "QA Tools Manager", "Salesforce QA Tester", "Software Development Engineer in Test", "Software QA Automation Engineer", "Software QA Engineer", "Software QA Manager", "Software Tester"],
    "Travel & Hospitality": ["Airline Travel Specialist", "Cruise Administration Support", "Cruise Agent", "Fraud Specialist", "GDS Flight Specialist", "GDS Team Leader", "Holiday Administrator", "Hotel Reservations Coordinator", "Inbound Cruise Sales Supervisor", "Online Reservation Processor", "Outbound Cruise Sales Supervisor", "Outbound Cruise Supervisor", "Supervisor, Cruise", "Supervisor, Cruise Sales", "Supervisor, GDS", "Supervisor, Travel", "Team Lead, Cruise", "Team Lead, GDS", "Team Lead, Travel", "Timeshare Specialist", "Travel Consultant", "Travel Contact Centre Manager", "Travel Service Desk Agent"],
    "Workforce Planning & Management": ["Capacity Planner", "Workforce Management Analyst", "Workforce Management Subject Matter Expert", "Workforce Planner"]
  };

  /* Placeholder monthly pricing anchors per category: [cloudstaff, US] */
  var PRICING = {
    "Accounting & Finance": [1738, 8251],
    "Administration, VA & Executive Support": [1628, 3871],
    "Architecture & Design": [2100, 8900],
    "Artificial Intelligence": [1848, 6483],
    "Banking & Financial Services": [1900, 7800],
    "Business Analysis & Product": [2300, 9600],
    "Cloud & Infrastructure": [2200, 10800],
    "Collections & Credit Control": [1500, 5200],
    "Construction & Estimating": [1950, 8200],
    "Creative & Multimedia": [1650, 6100],
    "Customer Service & Contact Centre": [1471, 5588],
    "Customer Success": [1800, 7200],
    "Cybersecurity": [2400, 11500],
    "Data & Analytics": [2050, 9200],
    "E-commerce": [1600, 5400],
    "Electronics & Embedded Systems": [2150, 9800],
    "Engineering": [2050, 9400],
    "Events & Experiences": [1550, 5600],
    "Executive Leadership": [4200, 18500],
    "Facilities & Workplace Services": [1500, 5900],
    "Healthcare Support": [1700, 6300],
    "Human Resources": [1700, 6900],
    "IT Support & Networks": [1750, 7600],
    "Learning, Development & Training": [1700, 6800],
    "Legal & Compliance": [1850, 8600],
    "Logistics & Supply Chain": [1700, 6700],
    "Marketing & Content": [1628, 5791],
    "Project Management & Operations": [2000, 8800],
    "Quality & Management Systems": [1800, 7400],
    "Real Estate & Property Services": [1600, 5700],
    "Recruitment & Talent Acquisition": [1900, 7900],
    "Sales & Business Development": [3049, 10115],
    "Software Development": [1958, 10379],
    "Software Testing & QA": [1850, 8700],
    "Travel & Hospitality": [1520, 5500],
    "Workforce Planning & Management": [1800, 7300]
  };

  var SENIOR_WORDS = /(senior|principal|director|head of|vp of|chief|manager|lead(er)?$)/i;

  var MODES = { office: { label: "Work From Office", mult: 1.09 },
                hybrid: { label: "Work Hybrid", mult: 1.04 },
                home: { label: "Work From Home", mult: 1.0 } };
  var COUNTRIES = { ph: { label: "Philippines", mult: 1.0 },
                    co: { label: "Colombia", mult: 1.18 },
                    in: { label: "India", mult: 1.05 } };
  var LEVELS = { junior: { label: "Junior", mult: 0.85 },
                 mid: { label: "Mid", mult: 1.0 },
                 senior: { label: "Senior", mult: 1.3 } };
  /* Placeholder FX rates, USD base */
  var CURRENCIES = { USD: { sym: "$", rate: 1.0 },
                     AUD: { sym: "A$", rate: 1.52 },
                     GBP: { sym: "\u00a3", rate: 0.79 },
                     HKD: { sym: "HK$", rate: 7.8 },
                     SGD: { sym: "S$", rate: 1.34 },
                     EUR: { sym: "\u20ac", rate: 0.92 },
                     NZD: { sym: "NZ$", rate: 1.66 },
                     CAD: { sym: "C$", rate: 1.37 } };
  var HOURS_PER_MONTH = 173.33;

  /* Deterministic per-role variation so prices look organic */
  function hash(s) {
    var h = 0;
    for (var i = 0; i < s.length; i++) { h = (h * 31 + s.charCodeAt(i)) >>> 0; }
    return h;
  }
  function basePrices(role, cat) {
    var p = PRICING[cat] || [1800, 7000];
    var v = 0.88 + (hash(role) % 25) / 100;           /* 0.88 .. 1.12 */
    var senior = SENIOR_WORDS.test(role) ? 1.35 : 1.0;
    return { cs: p[0] * v * senior, us: p[1] * v * senior };
  }
  function round10(n) { return Math.round(n / 10) * 10; }
  function fx(n) { return n * CURRENCIES[state.currency].rate; }
  function money(n) {
    return CURRENCIES[state.currency].sym + round10(fx(n)).toLocaleString("en-US");
  }
  function moneyHr(n) {
    return CURRENCIES[state.currency].sym +
      fx(n).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  /* Templated 10-line job description */
  function jd(role, cat) {
    var a = "an";
    if (!/^[AEIOU]/i.test(role)) a = "a";
    return [
      "<strong>" + role + "</strong>, " + cat,
      "Engage " + a + " experienced, English-fluent " + role +
        " who works your business hours as a dedicated, full-time member of your team.",
      "<em>Typical responsibilities:</em>",
      "• Own day-to-day " + cat.toLowerCase() + " tasks and deliverables to agreed KPIs",
      "• Follow your documented workflows, tools, and quality standards",
      "• Collaborate daily with your onshore team via your channels",
      "• Report progress with clear, structured updates",
      "• Identify process improvements and support your AI-enabled tooling",
      "<em>Includes:</em> recruitment, HR, payroll, managed equipment, security, and 24x7 IT support.",
      "Typical start: 15–25 days from kickoff."
    ].join("<br>");
  }

  /* ------------------------------------------------------------------ */
  /* State                                                               */
  /* ------------------------------------------------------------------ */
  var state = { mode: "office", country: "ph", currency: "USD", team: {} };  /* team: role -> {cat, qty, level} */

  /* ------------------------------------------------------------------ */
  /* DOM                                                                 */
  /* ------------------------------------------------------------------ */
  var $ = function (sel, el) { return (el || document).querySelector(sel); };
  var catalogEl = $("#tb-catalog"), teamEl = $("#tb-team"),
      totalsEl = $("#tb-totals"), searchEl = $("#tb-search"),
      countEl = $("#tb-role-count"), emptyEl = $("#tb-empty"),
      tipEl = $("#tb-tip");
  if (!catalogEl) return;

  var totalRoles = 0;
  Object.keys(CATALOG).forEach(function (c) { totalRoles += CATALOG[c].length; });
  if (countEl) countEl.textContent = totalRoles.toLocaleString("en-US");

  /* Build master controls */
  function buildSegmented(elId, options, key) {
    var el = $(elId);
    Object.keys(options).forEach(function (k) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "tb-seg-btn" + (state[key] === k ? " is-active" : "");
      b.textContent = options[k].label;
      b.addEventListener("click", function () {
        state[key] = k;
        el.querySelectorAll(".tb-seg-btn").forEach(function (x) { x.classList.remove("is-active"); });
        b.classList.add("is-active");
        renderTeam();
      });
      el.appendChild(b);
    });
  }
  buildSegmented("#tb-mode", MODES, "mode");
  buildSegmented("#tb-country", COUNTRIES, "country");
  var curEl = $("#tb-currency");
  if (curEl) {
    Object.keys(CURRENCIES).forEach(function (c) {
      var o = document.createElement("option");
      o.value = c;
      o.textContent = c;
      if (c === state.currency) o.selected = true;
      curEl.appendChild(o);
    });
    curEl.addEventListener("change", function () {
      state.currency = curEl.value;
      renderTeam();
    });
  }

  /* Build catalog */
  Object.keys(CATALOG).forEach(function (cat, idx) {
    var det = document.createElement("details");
    det.className = "tb-cat";
    if (idx === 0) det.open = true;
    var sum = document.createElement("summary");
    sum.innerHTML = '<span>' + cat + '</span><span class="badge">' + CATALOG[cat].length + " roles</span>";
    det.appendChild(sum);
    var list = document.createElement("div");
    list.className = "tb-role-list";
    CATALOG[cat].forEach(function (role) {
      var row = document.createElement("div");
      row.className = "tb-role";
      row.setAttribute("data-role", role.toLowerCase());
      var name = document.createElement("span");
      name.className = "tb-role-name";
      name.textContent = role;
      var add = document.createElement("button");
      add.type = "button";
      add.className = "tb-add";
      add.innerHTML = "+";
      add.title = "Add " + role;
      add.setAttribute("aria-label", "Add " + role + " to your team");
      add.addEventListener("click", function () { addRole(role, cat); });
      row.appendChild(name);
      row.appendChild(add);
      row.addEventListener("mouseenter", function (e) { showTip(role, cat, row); });
      row.addEventListener("mouseleave", hideTip);
      list.appendChild(row);
    });
    det.appendChild(list);
    /* Accordion: opening one category closes the others */
    det.addEventListener("toggle", function () {
      if (det.open) {
        catalogEl.querySelectorAll(".tb-cat[open]").forEach(function (other) {
          if (other !== det) other.open = false;
        });
      }
    });
    catalogEl.appendChild(det);
  });

  /* Tooltip */
  function showTip(role, cat, row) {
    if (!tipEl) return;
    tipEl.innerHTML = jd(role, cat);
    tipEl.hidden = false;
    var r = row.getBoundingClientRect();
    var top = r.top + window.scrollY;
    var tipH = tipEl.offsetHeight;
    if (r.top + tipH + 20 > window.innerHeight) top = top - tipH + r.height;
    tipEl.style.top = top + "px";
    tipEl.style.left = Math.min(r.right + 12, window.innerWidth - 360) + "px";
  }
  function hideTip() { if (tipEl) tipEl.hidden = true; }

  /* Search */
  if (searchEl) {
    searchEl.addEventListener("input", function () {
      var q = searchEl.value.trim().toLowerCase();
      catalogEl.querySelectorAll(".tb-cat").forEach(function (det) {
        var any = false;
        det.querySelectorAll(".tb-role").forEach(function (row) {
          var show = !q || row.getAttribute("data-role").indexOf(q) !== -1;
          row.style.display = show ? "" : "none";
          if (show) any = true;
        });
        det.style.display = any ? "" : "none";
        if (q && any) det.open = true;
      });
    });
  }

  /* Team management */
  function addRole(role, cat) {
    if (state.team[role]) state.team[role].qty += 1;
    else state.team[role] = { cat: cat, qty: 1, level: "mid" };
    renderTeam();
  }
  function renderTeam() {
    var roles = Object.keys(state.team);
    teamEl.innerHTML = "";
    if (emptyEl) emptyEl.hidden = roles.length > 0;
    var mMult = MODES[state.mode].mult, cMult = COUNTRIES[state.country].mult;
    var totalCs = 0, totalUs = 0;
    roles.forEach(function (role) {
      var item = state.team[role];
      if (!item.level) item.level = "mid";
      var p = basePrices(role, item.cat);
      var lMult = LEVELS[item.level].mult;
      var allIn = p.cs * mMult * cMult * lMult;
      var hourly = allIn / HOURS_PER_MONTH;
      totalCs += allIn * item.qty;
      totalUs += p.us * lMult * item.qty;

      var levelBtns = Object.keys(LEVELS).map(function (k) {
        return '<button type="button" class="tb-lvl-btn' +
          (item.level === k ? " is-active" : "") + '" data-lvl="' + k + '">' +
          LEVELS[k].label + "</button>";
      }).join("");

      var li = document.createElement("div");
      li.className = "tb-team-item";
      li.innerHTML =
        '<div class="tb-team-info"><strong>' + role + "</strong>" +
        '<span class="tb-team-cat">' + item.cat + "</span></div>" +
        '<div class="tb-team-controls">' +
        '<div class="tb-lvl" role="group" aria-label="Experience level for ' + role + '">' + levelBtns + "</div>" +
        '<div class="tb-qty" aria-label="Quantity for ' + role + '">' +
        '<button type="button" class="tb-qty-btn" data-d="-1" aria-label="Decrease">&minus;</button>' +
        '<span class="tb-qty-n">' + item.qty + "</span>" +
        '<button type="button" class="tb-qty-btn" data-d="1" aria-label="Increase">+</button>' +
        "</div>" +
        '<span class="tb-price">' + money(allIn * item.qty) + '/mo</span>' +
        '<button type="button" class="tb-remove" aria-label="Remove ' + role + '">&times;</button>' +
        "</div>" +
        '<div class="tb-hourly">All-in hourly rate: <strong>' + moneyHr(hourly) + '/hr</strong> per person</div>';
      li.querySelectorAll(".tb-lvl-btn").forEach(function (b) {
        b.addEventListener("click", function () {
          item.level = b.getAttribute("data-lvl");
          renderTeam();
        });
      });
      li.querySelectorAll(".tb-qty-btn").forEach(function (b) {
        b.addEventListener("click", function () {
          item.qty += parseInt(b.getAttribute("data-d"), 10);
          if (item.qty <= 0) delete state.team[role];
          renderTeam();
        });
      });
      li.querySelector(".tb-remove").addEventListener("click", function () {
        delete state.team[role];
        renderTeam();
      });
      teamEl.appendChild(li);
    });
    if (totalsEl) {
      totalsEl.hidden = roles.length === 0;
      $("#tb-total-cost").textContent = money(totalCs) + "/mo";
      $("#tb-total-saved").textContent = money(Math.max(0, totalUs - totalCs)) + "/mo";
      var seats = roles.reduce(function (n, r) { return n + state.team[r].qty; }, 0);
      $("#tb-total-seats").textContent = seats + (seats === 1 ? " team member" : " team members");
    }
  }
  renderTeam();
})();
