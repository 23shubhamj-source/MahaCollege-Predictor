# MahaCollege Predictor 2026
## Maharashtra Engineering Admission Assistant

A comprehensive, data-driven college prediction platform for Maharashtra MHT-CET CAP engineering admissions.

---

## 🚀 Quick Start

This is a **self-contained single-file web application** — no installation, server, or build step required.

### Open the Application

Simply open `index.html` in any modern web browser:

```
Double-click: index.html
```

Or serve it locally:
```bash
# Python 3
python -m http.server 8080

# Node.js
npx serve .
```

Then visit: http://localhost:8080

---

## 📊 Data

### Source
- **Primary Source:** Maharashtra State Common Entrance Test Cell
- **Official Portal:** https://cetcell.mahacet.org/
- **Admission Year:** 2025-26
- **CAP Rounds:** CAP Round 1, 2, and 3

### Coverage
| Metric | Count |
|--------|-------|
| Engineering Colleges | 379 |
| Branch-College Combinations | ~2,300+ |
| Cutoff Records | ~79,752 |
| CAP Rounds | 3 |
| Districts Covered | All Maharashtra |

### Category Codes
The data uses compact category codes. Format: `[Prefix][Category][Suffix]`

**Prefixes:**
- `G` = Government/General seats
- `L` = Linguistic Minority seats

**Base Categories:**
- `OPEN` = Open category
- `SC` = Scheduled Caste
- `ST` = Scheduled Tribe
- `VJ` = Vimukta Jati (DT-A)
- `NT1` = Nomadic Tribe 1 (DT-B)
- `NT2` = Nomadic Tribe 2 (DT-C)
- `NT3` = Nomadic Tribe 3 (DT-D)
- `OBC` = Other Backward Class
- `SEBC` = Socially & Educationally Backward Class
- `EWS` = Economically Weaker Section

**Suffixes:**
- `S` = State Level
- `H` = Home University
- `O` = Other University
- `N` = No restriction

**Special codes:** `TFWS` (Tuition Fee Waiver Scheme), `EWS`, `ORPHAN`, `DEF` (Defence), `PWD` (Person with Disability)

---

## 🎯 Features

### College Predictor
- Enter your MHT-CET percentile
- Select branch, category, and seat type
- View Ambitious / Target / Safer college recommendations
- Based on 2025-26 official CAP cutoff data

### Explore Colleges
- Browse all 379 engineering colleges
- Filter by district, branch, institute type
- Live search by name or code
- Paginated results

### College Details
- Full college profile
- All available branches
- Category-wise CAP Round 1/2/3 cutoff history
- Interactive charts (Chart.js)

### College Comparison
- Compare 2-4 colleges side by side
- Cross-college cutoff comparison for selected branch/category/round

### CAP Cutoffs Browser
- Browse all 79,000+ cutoff records
- Filter by institute, branch, category, round
- Export filtered data as CSV

### Admission Guide
- How MHT-CET CAP works
- Understanding percentile vs percentage
- Category and seat type explanations
- Why historical cutoffs ≠ future guarantees

---

## ⚠️ Important Disclaimer

**This is an independent student assistance platform. It is NOT affiliated with, endorsed by, or part of the Maharashtra CET Cell or any government authority.**

- Data represents 2025-26 CAP admission records.
- Historical cutoffs are reference points only.
- Actual 2026-27 admission depends on current year demand, seat availability, and official cutoffs.
- Always verify information from the official Maharashtra CET Cell website: https://cetcell.mahacet.org/

---

## 🏗️ Architecture

```
mahacollege-predictor-2026/
├── index.html          # Complete single-file application (~4-5MB with data)
├── README.md           # This file
└── src/
    └── data/
        └── data.js     # Raw extracted DATA object (reference copy)
```

### Technology Stack
- **Frontend:** Vanilla JavaScript (ES6+) with hash-based SPA routing
- **Styling:** Inline CSS with CSS custom properties (liquid glass theme)
- **Charts:** Chart.js 4.4.4 (CDN)
- **Fonts:** Google Fonts (Plus Jakarta Sans + Inter)
- **Data:** Embedded JavaScript object (no API calls)

### Data Flow
```
DATA object (embedded) → Build Indexes on load → User Input → Filter & Match → Display Results
```

### Indexes Built at Startup
- `INST_MAP`: institute code → array index
- `INST_BRANCHES`: institute index → branch indices
- `BRANCH_NAME_MAP`: branch name → branch indices
- `UNIQUE_BRANCHES`: sorted unique branch names
- `UNIQUE_CITIES`: sorted unique cities

---

## 🔄 Updating Data

To update with a new admission year's data:

1. Obtain official CAP allotment lists from Maharashtra CET Cell
2. Parse the data to match the schema:
   - `institutes`: `[code, name, type, city]`
   - `branches`: `[branchCode, instituteIndex, branchName]`
   - `cutoffs`: `[branchIndex, categoryCode, capRound, percentile, rank]`
3. Replace the `DATA` object in `index.html` (search for `const DATA = {`)
4. Update the data year references in the UI

For a Python-based data import pipeline, use the reference scripts in `src/data/`.

---

## 🧪 Testing

### Manual Test Cases

| # | Test | Expected |
|---|------|----------|
| 1 | Enter percentile 95 | Valid, shows results |
| 2 | Enter percentile 105 | Error: "must be between 0-100" |
| 3 | Enter text in percentile | Error: "please enter a valid number" |
| 4 | Select "Computer Engineering" branch | Filters to CS/CE branches |
| 5 | Select SC category | Shows SC category cutoffs |
| 6 | Search "Pune" in explore | Shows Pune colleges |
| 7 | Click college card | Navigates to detail page |
| 8 | Add 2 colleges to compare | Shows comparison table |
| 9 | Export CSV from cutoffs | Downloads CSV file |
| 10 | Toggle dark/light theme | Theme changes |
| 11 | Mobile viewport (<768px) | Responsive layout |
| 12 | Back button navigation | Hash routing works |

---

## 🌐 Browser Compatibility

- Chrome 90+ ✅
- Firefox 88+ ✅
- Safari 14+ ✅
- Edge 90+ ✅

Requires: `backdrop-filter` CSS support for glass effects (degrades gracefully).

---

## 📋 What's Implemented

- [x] Liquid glass premium UI (dark/light theme)
- [x] SPA hash routing
- [x] College Predictor (percentile-based)
- [x] Ambitious/Target/Safer classification
- [x] College Explorer with filters and pagination
- [x] College Detail pages with cutoff charts
- [x] College Comparison tool
- [x] CAP Cutoffs Browser with CSV export
- [x] Admission Guide
- [x] Mobile responsive design
- [x] Live search
- [x] Toast notifications
- [x] Data transparency section
- [x] Official CET Cell attribution

## 📋 What Requires Additional Configuration

- [ ] **Official college websites**: URLs not in the data source; linked to CET Cell search
- [ ] **Backend API**: Not required for this version (data is embedded)
- [ ] **Admin data import**: For future versions with backend
- [ ] **Automated data updates**: Requires a backend + cron job
- [ ] **User accounts**: Not implemented (no server)
- [ ] **2026-27 data**: Will be available from CET Cell after the admission process

---

## 📜 License & Attribution

Data sourced from: Maharashtra State Common Entrance Test Cell — https://cetcell.mahacet.org/

This platform is an independent educational tool. Not for commercial use without proper authorization.
