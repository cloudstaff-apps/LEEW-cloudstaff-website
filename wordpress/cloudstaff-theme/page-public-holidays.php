<?php
/**
 * Template Name: Public Holiday Planner
 * Template Post Type: page
 *
 * Generated from src/partials/public-holidays.html by build.py — edit the partial,
 * not this file, then re-run `python3 build.py`.
 *
 * @package Cloudstaff
 */

get_header();
?>
<main class="site-main" id="main-content">
<section class="site-hero">
  <div class="site-band-inner">
    <div class="site-hero-copy">
    <span class="eyebrow">Planning tool</span>
    <h1>Public holiday planner</h1>
    <p>Your Cloudstaffers have their own public holidays, and they rarely line up with yours. Choose where your team is based and where you are, and see which days they work and which days they take off across the year.</p>
    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="button button-lg">Talk to an expert</a>
    </div>
  </div>
</section>

<section class="site-band">
  <div class="site-band-inner">
    <div>
      <span class="eyebrow">Interactive tool</span>
      <h2>Whose public holidays should your team take?</h2>
      <p>Most clients ask their team to work through local public holidays and take the client's public holidays instead, so everyone is off on the same days. Only holidays that fall Monday to Friday need to be swapped.</p>

      <div class="coverage-tool hol-tool" id="hol-tool">
        <div class="hol-controls card">
          <div class="cov-control">
            <span class="cov-label">Which holidays should your team take off?</span>
            <div class="tb-seg" id="hol-mode" role="group" aria-label="Holiday preference"></div>
          </div>
          <div class="cov-control">
            <span class="cov-label">Where are your Cloudstaffers?</span>
            <div class="tb-seg" id="hol-staff" role="group" aria-label="Service country"></div>
          </div>
          <div class="cov-control">
            <span class="cov-label">Your country</span>
            <div class="tb-seg" id="hol-country" role="group" aria-label="Your country"></div>
          </div>
          <div class="cov-control">
            <label class="cov-label" for="hol-region" id="hol-region-label">State or region</label>
            <select class="select" id="hol-region"></select>
          </div>
        </div>

        <div class="hol-tiles" id="hol-tiles" aria-live="polite"></div>
        <div class="card hol-table" id="hol-table" aria-live="polite"></div>
        <p class="cov-note" id="hol-note"></p>
      </div>
    </div>
  </div>
</section>

<!-- Holiday data for the planner. Dates are MM-DD within "year". "t": 1 marks a
     date that is not final. Edit this block to add a country, a region or a year. -->
<script type="application/json" id="hol-data">
{
 "version": "1.1",
 "year": 2027,
 "staff": {
  "ph": {
   "label": "Philippines",
   "flag": "ph",
   "source": "Proclamation No. 1427 (September 2026)",
   "h": [
    {
     "d": "01-01",
     "n": "New Year's Day"
    },
    {
     "d": "02-06",
     "n": "Chinese New Year"
    },
    {
     "d": "03-10",
     "n": "Eid'l Fitr",
     "t": 1,
     "note": "Not yet proclaimed. Estimated date"
    },
    {
     "d": "03-25",
     "n": "Maundy Thursday"
    },
    {
     "d": "03-26",
     "n": "Good Friday"
    },
    {
     "d": "03-27",
     "n": "Black Saturday"
    },
    {
     "d": "04-09",
     "n": "Araw ng Kagitingan (Day of Valor)"
    },
    {
     "d": "05-01",
     "n": "Labor Day"
    },
    {
     "d": "05-17",
     "n": "Eid'l Adha",
     "t": 1,
     "note": "Not yet proclaimed. Estimated date"
    },
    {
     "d": "06-12",
     "n": "Independence Day"
    },
    {
     "d": "08-21",
     "n": "Ninoy Aquino Day"
    },
    {
     "d": "08-30",
     "n": "National Heroes Day"
    },
    {
     "d": "11-01",
     "n": "All Saints' Day"
    },
    {
     "d": "11-02",
     "n": "All Souls' Day"
    },
    {
     "d": "11-30",
     "n": "Bonifacio Day"
    },
    {
     "d": "12-08",
     "n": "Feast of the Immaculate Conception"
    },
    {
     "d": "12-24",
     "n": "Christmas Eve"
    },
    {
     "d": "12-25",
     "n": "Christmas Day"
    },
    {
     "d": "12-30",
     "n": "Rizal Day"
    },
    {
     "d": "12-31",
     "n": "Last Day of the Year"
    }
   ]
  },
  "in": {
   "label": "India",
   "flag": "in",
   "source": "Central Government gazetted holidays, DoPT memorandum of 16 July 2026",
   "h": [
    {
     "d": "01-26",
     "n": "Republic Day"
    },
    {
     "d": "03-10",
     "n": "Id-ul-Fitr",
     "t": 1,
     "note": "Date depends on the moon sighting and may shift"
    },
    {
     "d": "03-23",
     "n": "Holi"
    },
    {
     "d": "03-26",
     "n": "Good Friday"
    },
    {
     "d": "04-15",
     "n": "Ram Navami"
    },
    {
     "d": "04-19",
     "n": "Mahavir Jayanti"
    },
    {
     "d": "05-17",
     "n": "Id-ul-Zuha (Bakrid)",
     "t": 1,
     "note": "Date depends on the moon sighting and may shift"
    },
    {
     "d": "05-20",
     "n": "Buddha Purnima"
    },
    {
     "d": "06-16",
     "n": "Muharram",
     "t": 1,
     "note": "Date depends on the moon sighting and may shift"
    },
    {
     "d": "08-15",
     "n": "Independence Day"
    },
    {
     "d": "08-15",
     "n": "Id-e-Milad",
     "t": 1,
     "note": "Date depends on the moon sighting and may shift"
    },
    {
     "d": "08-25",
     "n": "Janmashtami"
    },
    {
     "d": "10-02",
     "n": "Mahatma Gandhi's Birthday"
    },
    {
     "d": "10-09",
     "n": "Dussehra"
    },
    {
     "d": "10-29",
     "n": "Diwali"
    },
    {
     "d": "11-14",
     "n": "Guru Nanak's Birthday"
    },
    {
     "d": "12-25",
     "n": "Christmas Day"
    }
   ]
  },
  "co": {
   "label": "Colombia",
   "flag": "co",
   "source": "National holidays under Colombia's holiday law (Ley 51 of 1983)",
   "h": [
    {
     "d": "01-01",
     "n": "New Year's Day"
    },
    {
     "d": "01-11",
     "n": "Epiphany"
    },
    {
     "d": "03-22",
     "n": "Saint Joseph's Day"
    },
    {
     "d": "03-25",
     "n": "Maundy Thursday"
    },
    {
     "d": "03-26",
     "n": "Good Friday"
    },
    {
     "d": "05-01",
     "n": "Labor Day"
    },
    {
     "d": "05-10",
     "n": "Ascension Day"
    },
    {
     "d": "05-31",
     "n": "Corpus Christi"
    },
    {
     "d": "06-07",
     "n": "Sacred Heart"
    },
    {
     "d": "07-05",
     "n": "Saint Peter and Saint Paul"
    },
    {
     "d": "07-20",
     "n": "Independence Day"
    },
    {
     "d": "08-07",
     "n": "Battle of Boyaca"
    },
    {
     "d": "08-16",
     "n": "Assumption of Mary"
    },
    {
     "d": "10-18",
     "n": "Columbus Day (Dia de la Raza)"
    },
    {
     "d": "11-01",
     "n": "All Saints' Day"
    },
    {
     "d": "11-15",
     "n": "Independence of Cartagena"
    },
    {
     "d": "12-08",
     "n": "Immaculate Conception"
    },
    {
     "d": "12-25",
     "n": "Christmas Day"
    }
   ]
  },
  "ke": {
   "label": "Kenya",
   "flag": "ke",
   "source": "Public Holidays Act (Cap. 110)",
   "h": [
    {
     "d": "01-01",
     "n": "New Year's Day"
    },
    {
     "d": "03-10",
     "n": "Idd-ul-Fitr",
     "t": 1,
     "note": "Date depends on the moon sighting and may shift"
    },
    {
     "d": "03-26",
     "n": "Good Friday"
    },
    {
     "d": "03-29",
     "n": "Easter Monday"
    },
    {
     "d": "05-01",
     "n": "Labour Day"
    },
    {
     "d": "05-17",
     "n": "Idd-ul-Azha",
     "t": 1,
     "note": "Date depends on the moon sighting and may shift"
    },
    {
     "d": "06-01",
     "n": "Madaraka Day"
    },
    {
     "d": "10-10",
     "n": "Mazingira Day"
    },
    {
     "d": "10-11",
     "n": "Mazingira Day (observed)"
    },
    {
     "d": "10-20",
     "n": "Mashujaa Day"
    },
    {
     "d": "12-12",
     "n": "Jamhuri Day"
    },
    {
     "d": "12-13",
     "n": "Jamhuri Day (observed)"
    },
    {
     "d": "12-25",
     "n": "Christmas Day"
    },
    {
     "d": "12-26",
     "n": "Utamaduni Day (Boxing Day)"
    },
    {
     "d": "12-27",
     "n": "Utamaduni Day (observed)"
    }
   ]
  }
 },
 "clients": {
  "us": {
   "label": "USA",
   "flag": "us",
   "regionLabel": "State",
   "source": "US federal holidays (OPM schedule) plus state government holidays set by state law",
   "base": [
    {
     "d": "01-01",
     "n": "New Year's Day"
    },
    {
     "d": "01-18",
     "n": "Martin Luther King Jr. Day"
    },
    {
     "d": "02-15",
     "n": "Presidents' Day (Washington's Birthday)"
    },
    {
     "d": "05-31",
     "n": "Memorial Day"
    },
    {
     "d": "06-18",
     "n": "Juneteenth (observed)"
    },
    {
     "d": "06-19",
     "n": "Juneteenth"
    },
    {
     "d": "07-04",
     "n": "Independence Day"
    },
    {
     "d": "07-05",
     "n": "Independence Day (observed)"
    },
    {
     "d": "09-06",
     "n": "Labor Day"
    },
    {
     "d": "10-11",
     "n": "Columbus Day"
    },
    {
     "d": "11-11",
     "n": "Veterans Day"
    },
    {
     "d": "11-25",
     "n": "Thanksgiving Day"
    },
    {
     "d": "12-24",
     "n": "Christmas Day (observed)"
    },
    {
     "d": "12-25",
     "n": "Christmas Day"
    },
    {
     "d": "12-31",
     "n": "New Year's Day 2028 (observed)"
    }
   ],
   "regions": {
    "fed": {
     "label": "Federal holidays only",
     "h": []
    },
    "al": {
     "label": "Alabama",
     "h": [
      {
       "d": "04-26",
       "n": "Confederate Memorial Day",
       "note": "State government holiday"
      },
      {
       "d": "06-07",
       "n": "Jefferson Davis' Birthday",
       "note": "State government holiday"
      }
     ]
    },
    "ak": {
     "label": "Alaska",
     "h": [
      {
       "d": "03-29",
       "n": "Seward's Day",
       "note": "State government holiday"
      },
      {
       "d": "10-18",
       "n": "Alaska Day",
       "note": "State government holiday"
      }
     ]
    },
    "az": {
     "label": "Arizona",
     "h": []
    },
    "ar": {
     "label": "Arkansas",
     "h": []
    },
    "ca": {
     "label": "California",
     "h": [
      {
       "d": "03-31",
       "n": "Cesar Chavez Day",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "co": {
     "label": "Colorado",
     "h": [
      {
       "d": "10-04",
       "n": "Frances Xavier Cabrini Day",
       "note": "State government holiday"
      }
     ]
    },
    "ct": {
     "label": "Connecticut",
     "h": [
      {
       "d": "02-12",
       "n": "Lincoln's Birthday",
       "note": "State government holiday"
      },
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      }
     ]
    },
    "de": {
     "label": "Delaware",
     "h": [
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "dc": {
     "label": "District of Columbia",
     "h": [
      {
       "d": "04-16",
       "n": "DC Emancipation Day",
       "note": "District government holiday"
      }
     ]
    },
    "fl": {
     "label": "Florida",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "ga": {
     "label": "Georgia",
     "h": [
      {
       "d": "11-26",
       "n": "State Holiday (day after Thanksgiving)",
       "note": "State government holiday"
      }
     ]
    },
    "hi": {
     "label": "Hawaii",
     "h": [
      {
       "d": "03-26",
       "n": "Prince Kuhio Day",
       "note": "State government holiday"
      },
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      },
      {
       "d": "06-11",
       "n": "King Kamehameha I Day",
       "note": "State government holiday"
      },
      {
       "d": "08-20",
       "n": "Statehood Day",
       "note": "State government holiday"
      }
     ]
    },
    "id": {
     "label": "Idaho",
     "h": []
    },
    "il": {
     "label": "Illinois",
     "h": [
      {
       "d": "02-12",
       "n": "Lincoln's Birthday",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "in": {
     "label": "Indiana",
     "h": [
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      },
      {
       "d": "05-04",
       "n": "Primary Election Day",
       "note": "State government holiday"
      },
      {
       "d": "11-02",
       "n": "General Election Day",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Lincoln's Birthday (observed day after Thanksgiving)",
       "note": "State government holiday"
      }
     ]
    },
    "ia": {
     "label": "Iowa",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "ks": {
     "label": "Kansas",
     "h": []
    },
    "ky": {
     "label": "Kentucky",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "la": {
     "label": "Louisiana",
     "h": [
      {
       "d": "02-09",
       "n": "Mardi Gras",
       "note": "State government holiday"
      },
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      }
     ]
    },
    "me": {
     "label": "Maine",
     "h": [
      {
       "d": "04-19",
       "n": "Patriots' Day",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "md": {
     "label": "Maryland",
     "h": [
      {
       "d": "11-26",
       "n": "American Indian Heritage Day",
       "note": "State government holiday"
      }
     ]
    },
    "ma": {
     "label": "Massachusetts",
     "h": [
      {
       "d": "04-19",
       "n": "Patriots' Day",
       "note": "State government holiday"
      }
     ]
    },
    "mi": {
     "label": "Michigan",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "mn": {
     "label": "Minnesota",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "ms": {
     "label": "Mississippi",
     "h": [
      {
       "d": "04-26",
       "n": "Confederate Memorial Day",
       "note": "State government holiday"
      }
     ]
    },
    "mo": {
     "label": "Missouri",
     "h": [
      {
       "d": "02-12",
       "n": "Lincoln's Birthday",
       "note": "State government holiday"
      },
      {
       "d": "05-08",
       "n": "Truman Day",
       "note": "State government holiday"
      },
      {
       "d": "05-07",
       "n": "Truman Day (observed)",
       "note": "State government holiday"
      }
     ]
    },
    "mt": {
     "label": "Montana",
     "h": []
    },
    "ne": {
     "label": "Nebraska",
     "h": [
      {
       "d": "04-30",
       "n": "Arbor Day",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "nv": {
     "label": "Nevada",
     "h": [
      {
       "d": "10-29",
       "n": "Nevada Day",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Family Day",
       "note": "State government holiday"
      }
     ]
    },
    "nh": {
     "label": "New Hampshire",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "nj": {
     "label": "New Jersey",
     "h": [
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      },
      {
       "d": "11-02",
       "n": "Election Day",
       "note": "State government holiday"
      }
     ]
    },
    "nm": {
     "label": "New Mexico",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "ny": {
     "label": "New York",
     "h": [
      {
       "d": "02-12",
       "n": "Lincoln's Birthday",
       "note": "State government holiday"
      },
      {
       "d": "11-02",
       "n": "Election Day",
       "note": "State government holiday"
      }
     ]
    },
    "nc": {
     "label": "North Carolina",
     "h": [
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "nd": {
     "label": "North Dakota",
     "h": [
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      }
     ]
    },
    "oh": {
     "label": "Ohio",
     "h": []
    },
    "ok": {
     "label": "Oklahoma",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "or": {
     "label": "Oregon",
     "h": []
    },
    "pa": {
     "label": "Pennsylvania",
     "h": [
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "ri": {
     "label": "Rhode Island",
     "h": [
      {
       "d": "08-09",
       "n": "Victory Day",
       "note": "State government holiday"
      }
     ]
    },
    "sc": {
     "label": "South Carolina",
     "h": [
      {
       "d": "05-10",
       "n": "Confederate Memorial Day",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "sd": {
     "label": "South Dakota",
     "h": []
    },
    "tn": {
     "label": "Tennessee",
     "h": [
      {
       "d": "03-26",
       "n": "Good Friday",
       "note": "State government holiday"
      }
     ]
    },
    "tx": {
     "label": "Texas",
     "h": [
      {
       "d": "01-19",
       "n": "Confederate Heroes Day",
       "note": "State partial staffing holiday"
      },
      {
       "d": "03-02",
       "n": "Texas Independence Day",
       "note": "State partial staffing holiday"
      },
      {
       "d": "04-21",
       "n": "San Jacinto Day",
       "note": "State partial staffing holiday"
      },
      {
       "d": "08-27",
       "n": "Lyndon Baines Johnson Day",
       "note": "State partial staffing holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "ut": {
     "label": "Utah",
     "h": [
      {
       "d": "07-24",
       "n": "Pioneer Day",
       "note": "State government holiday"
      },
      {
       "d": "07-23",
       "n": "Pioneer Day (observed)",
       "note": "State government holiday"
      }
     ]
    },
    "vt": {
     "label": "Vermont",
     "h": [
      {
       "d": "03-02",
       "n": "Town Meeting Day",
       "note": "State government holiday"
      },
      {
       "d": "08-16",
       "n": "Bennington Battle Day",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "va": {
     "label": "Virginia",
     "h": [
      {
       "d": "11-02",
       "n": "Election Day",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Day after Thanksgiving",
       "note": "State government holiday"
      }
     ]
    },
    "wa": {
     "label": "Washington",
     "h": [
      {
       "d": "11-26",
       "n": "Native American Heritage Day",
       "note": "State government holiday"
      }
     ]
    },
    "wv": {
     "label": "West Virginia",
     "h": [
      {
       "d": "06-20",
       "n": "West Virginia Day",
       "note": "State government holiday"
      },
      {
       "d": "06-21",
       "n": "West Virginia Day (observed)",
       "note": "State government holiday"
      },
      {
       "d": "11-26",
       "n": "Lincoln's Day (day after Thanksgiving)",
       "note": "State government holiday"
      }
     ]
    },
    "wi": {
     "label": "Wisconsin",
     "h": []
    },
    "wy": {
     "label": "Wyoming",
     "h": []
    }
   }
  },
  "au": {
   "label": "Australia",
   "flag": "au",
   "regionLabel": "State or territory",
   "source": "Fair Work Ombudsman 2027 public holidays list",
   "base": [],
   "regions": {
    "nsw": {
     "label": "New South Wales",
     "h": [
      {
       "d": "01-01",
       "n": "New Year's Day"
      },
      {
       "d": "01-26",
       "n": "Australia Day"
      },
      {
       "d": "03-26",
       "n": "Good Friday"
      },
      {
       "d": "03-27",
       "n": "Easter Saturday"
      },
      {
       "d": "03-28",
       "n": "Easter Sunday"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "04-25",
       "n": "Anzac Day"
      },
      {
       "d": "04-26",
       "n": "Anzac Day (additional day)"
      },
      {
       "d": "12-25",
       "n": "Christmas Day"
      },
      {
       "d": "12-26",
       "n": "Boxing Day"
      },
      {
       "d": "12-27",
       "n": "Christmas Day (additional day)"
      },
      {
       "d": "12-28",
       "n": "Boxing Day (additional day)"
      },
      {
       "d": "06-14",
       "n": "King's Birthday"
      },
      {
       "d": "10-04",
       "n": "Labour Day"
      }
     ]
    },
    "vic": {
     "label": "Victoria",
     "h": [
      {
       "d": "01-01",
       "n": "New Year's Day"
      },
      {
       "d": "01-26",
       "n": "Australia Day"
      },
      {
       "d": "03-26",
       "n": "Good Friday"
      },
      {
       "d": "03-27",
       "n": "Saturday before Easter Sunday"
      },
      {
       "d": "03-28",
       "n": "Easter Sunday"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "04-25",
       "n": "Anzac Day"
      },
      {
       "d": "12-25",
       "n": "Christmas Day"
      },
      {
       "d": "12-26",
       "n": "Boxing Day"
      },
      {
       "d": "12-27",
       "n": "Christmas Day (additional day)"
      },
      {
       "d": "12-28",
       "n": "Boxing Day (additional day)"
      },
      {
       "d": "03-08",
       "n": "Labour Day"
      },
      {
       "d": "06-14",
       "n": "King's Birthday"
      },
      {
       "d": "09-24",
       "n": "Friday before the AFL Grand Final",
       "t": 1,
       "note": "Depends on the AFL schedule. Estimated date"
      },
      {
       "d": "11-02",
       "n": "Melbourne Cup Day",
       "note": "Metropolitan Melbourne. Some regional areas differ"
      }
     ]
    },
    "qld": {
     "label": "Queensland",
     "h": [
      {
       "d": "01-01",
       "n": "New Year's Day"
      },
      {
       "d": "01-26",
       "n": "Australia Day"
      },
      {
       "d": "03-26",
       "n": "Good Friday"
      },
      {
       "d": "03-27",
       "n": "Day after Good Friday"
      },
      {
       "d": "03-28",
       "n": "Easter Sunday"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "04-26",
       "n": "Anzac Day"
      },
      {
       "d": "12-25",
       "n": "Christmas Day"
      },
      {
       "d": "12-26",
       "n": "Boxing Day"
      },
      {
       "d": "12-27",
       "n": "Christmas Day (additional day)"
      },
      {
       "d": "12-28",
       "n": "Boxing Day (additional day)"
      },
      {
       "d": "05-03",
       "n": "Labour Day"
      },
      {
       "d": "08-11",
       "n": "Royal Queensland Show",
       "note": "Brisbane area only"
      },
      {
       "d": "10-04",
       "n": "King's Birthday"
      }
     ]
    },
    "wa": {
     "label": "Western Australia",
     "h": [
      {
       "d": "01-01",
       "n": "New Year's Day"
      },
      {
       "d": "01-26",
       "n": "Australia Day"
      },
      {
       "d": "03-26",
       "n": "Good Friday"
      },
      {
       "d": "03-28",
       "n": "Easter Sunday"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "04-25",
       "n": "Anzac Day"
      },
      {
       "d": "04-26",
       "n": "Anzac Day (additional day)"
      },
      {
       "d": "12-25",
       "n": "Christmas Day"
      },
      {
       "d": "12-26",
       "n": "Boxing Day"
      },
      {
       "d": "12-27",
       "n": "Christmas Day (additional day)"
      },
      {
       "d": "12-28",
       "n": "Boxing Day (additional day)"
      },
      {
       "d": "03-01",
       "n": "Labour Day"
      },
      {
       "d": "06-07",
       "n": "Western Australia Day"
      },
      {
       "d": "09-27",
       "n": "King's Birthday",
       "note": "Some regional areas differ"
      }
     ]
    },
    "sa": {
     "label": "South Australia",
     "h": [
      {
       "d": "01-01",
       "n": "New Year's Day"
      },
      {
       "d": "01-26",
       "n": "Australia Day"
      },
      {
       "d": "03-26",
       "n": "Good Friday"
      },
      {
       "d": "03-27",
       "n": "Easter Saturday"
      },
      {
       "d": "03-28",
       "n": "Easter Sunday"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "04-25",
       "n": "Anzac Day"
      },
      {
       "d": "12-25",
       "n": "Christmas Day"
      },
      {
       "d": "12-26",
       "n": "Proclamation Day"
      },
      {
       "d": "12-27",
       "n": "Christmas Day (additional day)"
      },
      {
       "d": "12-28",
       "n": "Proclamation Day (additional day)"
      },
      {
       "d": "03-08",
       "n": "Adelaide Cup Day"
      },
      {
       "d": "06-14",
       "n": "King's Birthday"
      },
      {
       "d": "10-04",
       "n": "Labour Day"
      }
     ]
    },
    "tas": {
     "label": "Tasmania",
     "h": [
      {
       "d": "01-01",
       "n": "New Year's Day"
      },
      {
       "d": "01-26",
       "n": "Australia Day"
      },
      {
       "d": "03-08",
       "n": "Eight Hours Day"
      },
      {
       "d": "03-26",
       "n": "Good Friday"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "04-25",
       "n": "Anzac Day"
      },
      {
       "d": "06-14",
       "n": "King's Birthday"
      },
      {
       "d": "12-25",
       "n": "Christmas Day"
      },
      {
       "d": "12-27",
       "n": "Christmas Day (additional day)"
      },
      {
       "d": "12-28",
       "n": "Boxing Day"
      }
     ]
    },
    "act": {
     "label": "Australian Capital Territory",
     "h": [
      {
       "d": "01-01",
       "n": "New Year's Day"
      },
      {
       "d": "01-26",
       "n": "Australia Day"
      },
      {
       "d": "03-26",
       "n": "Good Friday"
      },
      {
       "d": "03-27",
       "n": "Easter Saturday"
      },
      {
       "d": "03-28",
       "n": "Easter Sunday"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "04-25",
       "n": "Anzac Day"
      },
      {
       "d": "04-26",
       "n": "Anzac Day (additional day)"
      },
      {
       "d": "12-25",
       "n": "Christmas Day"
      },
      {
       "d": "12-26",
       "n": "Boxing Day"
      },
      {
       "d": "12-27",
       "n": "Christmas Day (additional day)"
      },
      {
       "d": "12-28",
       "n": "Boxing Day (additional day)"
      },
      {
       "d": "03-08",
       "n": "Canberra Day"
      },
      {
       "d": "05-31",
       "n": "Reconciliation Day"
      },
      {
       "d": "06-14",
       "n": "King's Birthday"
      },
      {
       "d": "10-04",
       "n": "Labour Day"
      }
     ]
    },
    "nt": {
     "label": "Northern Territory",
     "h": [
      {
       "d": "01-01",
       "n": "New Year's Day"
      },
      {
       "d": "01-26",
       "n": "Australia Day"
      },
      {
       "d": "03-26",
       "n": "Good Friday"
      },
      {
       "d": "03-27",
       "n": "Easter Saturday"
      },
      {
       "d": "03-28",
       "n": "Easter Sunday"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "04-26",
       "n": "Anzac Day"
      },
      {
       "d": "12-25",
       "n": "Christmas Day"
      },
      {
       "d": "12-26",
       "n": "Boxing Day"
      },
      {
       "d": "12-27",
       "n": "Christmas Day (additional day)"
      },
      {
       "d": "12-28",
       "n": "Boxing Day (additional day)"
      },
      {
       "d": "05-03",
       "n": "May Day"
      },
      {
       "d": "06-14",
       "n": "King's Birthday"
      },
      {
       "d": "08-02",
       "n": "Picnic Day"
      }
     ]
    }
   }
  },
  "nz": {
   "label": "New Zealand",
   "flag": "nz",
   "regionLabel": "Region",
   "source": "Holidays Act 2003 rules. Employment New Zealand had not published its 2027 table at the time of writing",
   "base": [
    {
     "d": "01-01",
     "n": "New Year's Day"
    },
    {
     "d": "01-02",
     "n": "Day after New Year's Day"
    },
    {
     "d": "01-04",
     "n": "Day after New Year's Day (observed)"
    },
    {
     "d": "02-06",
     "n": "Waitangi Day"
    },
    {
     "d": "02-08",
     "n": "Waitangi Day (observed)"
    },
    {
     "d": "03-26",
     "n": "Good Friday"
    },
    {
     "d": "03-29",
     "n": "Easter Monday"
    },
    {
     "d": "04-25",
     "n": "Anzac Day"
    },
    {
     "d": "04-26",
     "n": "Anzac Day (observed)"
    },
    {
     "d": "06-07",
     "n": "King's Birthday"
    },
    {
     "d": "06-25",
     "n": "Matariki"
    },
    {
     "d": "10-25",
     "n": "Labour Day"
    },
    {
     "d": "12-25",
     "n": "Christmas Day"
    },
    {
     "d": "12-26",
     "n": "Boxing Day"
    },
    {
     "d": "12-27",
     "n": "Christmas Day (observed)"
    },
    {
     "d": "12-28",
     "n": "Boxing Day (observed)"
    }
   ],
   "regions": {
    "akl": {
     "label": "Auckland and Northland",
     "h": [
      {
       "d": "02-01",
       "n": "Auckland Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "wgn": {
     "label": "Wellington",
     "h": [
      {
       "d": "01-25",
       "n": "Wellington Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "can": {
     "label": "Canterbury",
     "h": [
      {
       "d": "11-12",
       "n": "Canterbury Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "ota": {
     "label": "Otago",
     "h": [
      {
       "d": "03-22",
       "n": "Otago Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "stl": {
     "label": "Southland",
     "h": [
      {
       "d": "03-30",
       "n": "Southland Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "tki": {
     "label": "Taranaki",
     "h": [
      {
       "d": "03-08",
       "n": "Taranaki Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "hkb": {
     "label": "Hawke's Bay",
     "h": [
      {
       "d": "10-22",
       "n": "Hawke's Bay Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "nsn": {
     "label": "Nelson",
     "h": [
      {
       "d": "02-01",
       "n": "Nelson Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "mbh": {
     "label": "Marlborough",
     "h": [
      {
       "d": "11-01",
       "n": "Marlborough Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "sca": {
     "label": "South Canterbury",
     "h": [
      {
       "d": "09-27",
       "n": "South Canterbury Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "wtl": {
     "label": "Westland",
     "h": [
      {
       "d": "11-29",
       "n": "Westland Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    },
    "cit": {
     "label": "Chatham Islands",
     "h": [
      {
       "d": "11-29",
       "n": "Chatham Islands Anniversary Day",
       "note": "Regional anniversary day"
      }
     ]
    }
   }
  },
  "uk": {
   "label": "UK",
   "flag": "gb",
   "regionLabel": "Nation",
   "source": "GOV.UK bank holidays",
   "base": [
    {
     "d": "01-01",
     "n": "New Year's Day"
    },
    {
     "d": "03-26",
     "n": "Good Friday"
    },
    {
     "d": "05-03",
     "n": "Early May bank holiday"
    },
    {
     "d": "05-31",
     "n": "Spring bank holiday"
    },
    {
     "d": "12-25",
     "n": "Christmas Day"
    },
    {
     "d": "12-26",
     "n": "Boxing Day"
    },
    {
     "d": "12-27",
     "n": "Christmas Day (substitute day)"
    },
    {
     "d": "12-28",
     "n": "Boxing Day (substitute day)"
    }
   ],
   "regions": {
    "ew": {
     "label": "England and Wales",
     "h": [
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "08-30",
       "n": "Summer bank holiday"
      }
     ]
    },
    "sc": {
     "label": "Scotland",
     "h": [
      {
       "d": "01-02",
       "n": "2nd January"
      },
      {
       "d": "01-04",
       "n": "2nd January (substitute day)"
      },
      {
       "d": "08-02",
       "n": "Summer bank holiday"
      },
      {
       "d": "11-30",
       "n": "St Andrew's Day"
      }
     ]
    },
    "ni": {
     "label": "Northern Ireland",
     "h": [
      {
       "d": "03-17",
       "n": "St Patrick's Day"
      },
      {
       "d": "03-29",
       "n": "Easter Monday"
      },
      {
       "d": "07-12",
       "n": "Battle of the Boyne (Orangemen's Day)"
      },
      {
       "d": "08-30",
       "n": "Summer bank holiday"
      }
     ]
    }
   }
  }
 }
}
</script>
<script src="<?php echo esc_url( get_template_directory_uri() . '/holidays.js' ); ?>" defer></script>

<section class="site-cta">
  <div class="site-band-inner">
    <h2>Plan the year with your team</h2>
    <p>Tell us which calendar you want your team to follow and we will set it up with them before the year starts.</p>
    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="button button-inverse button-lg">Talk to an expert</a>
  </div>
</section>

</main>
<?php
get_footer();
