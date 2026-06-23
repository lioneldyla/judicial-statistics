# Judicial Statistics — Côte d'Ivoire

> Data pipelines, analysis tools and methodology for the national Judicial Statistics Yearbooks published by the Ministry of Justice of Côte d'Ivoire.

[![Author](https://img.shields.io/badge/Author-Yoboukoua_DJORO-0077B5?style=flat)](https://www.linkedin.com/in/lioneldyla/)
[![Domain](https://img.shields.io/badge/Domain-Judicial_Statistics-green?style=flat)]()
[![Publications](https://img.shields.io/badge/Publications-2019_·_2023-lightgrey?style=flat)]()

---

## Overview

This repository documents the data methodology, collection tools, and analytical pipelines used to produce the **national Judicial Statistics Yearbooks** for Côte d'Ivoire's Ministry of Justice.

The Judicial Statistics Yearbook is the primary official reference for justice sector data in Côte d'Ivoire — covering criminal, civil, commercial, and administrative cases across all court levels.

---

## Publications

| Year | Title | Publisher | Scope |
|---|---|---|---|
| 2023 | Judicial and Penitentiary Statistics Yearbook | Directorate of Planning — Ministry of Justice | Courts + Penitentiary system |
| 2019 | Judicial Statistics Yearbook | Ministry of Justice | All court levels |

---

## Data Coverage

### Court Levels
- Tribunal de Première Instance (TPI)
- Tribunal de Commerce
- Cours d'Appel
- Cour de Cassation
- Tribunaux Militaires

### Case Categories
- Criminal matters (affaires pénales)
- Civil matters (affaires civiles)
- Commercial matters (affaires commerciales)
- Administrative matters
- Family law (affaires de famille)

### Penitentiary Data (2023 edition)
- Prison population by category
- Pre-trial detention rates
- Recidivism indicators
- Rehabilitation program metrics

---

## Methodology

```
Data Collection
  └── Court registries (greffes) → standardized forms
  └── Statistical questionnaires to 30+ jurisdictions
  └── Administrative records from penitentiary services

Data Processing
  └── Validation and quality checks
  └── Aggregation by jurisdiction, type, period
  └── Cross-tabulation and trend analysis

Data Visualization
  └── Power BI dashboards
  └── Statistical tables and charts
  └── Yearbook publication (PDF)
```

---

## Tools & Technologies

- **Python** — Data collection automation, cleaning, transformation
- **SQL** — Database queries and aggregation
- **Power BI** — Interactive dashboards and visualization
- **Excel** — Statistical forms and cross-tabulation
- **pandas** — Data manipulation and analysis

---

## Key Indicators Tracked

- Total cases filed per jurisdiction per year
- Case clearance rate and backlog
- Average processing time by case type
- Judge-to-case ratio
- Access to justice indicators (geographic distribution)
- Prison occupancy rate
- Pre-trial detention as % of total prison population

---

## Impact

These yearbooks serve as the primary data source for:
- National justice reform planning
- Budget allocation decisions
- International reporting (UN, World Bank, OHADA)
- Academic research on African justice systems
- Performance evaluation of judicial institutions

---

## Related Projects

- [jdgf-framework](https://github.com/lioneldyla/jdgf-framework) — Judicial Data Governance Framework
- [monitor-the-reactor](https://github.com/lioneldyla/monitor-the-reactor) — ML capstone project (Le Wagon 2025)

---

## Author

**Yoboukoua DJORO** — Deputy Director of Studies & Statistics | Head of IT & Statistics Services  
Ministry of Justice · Cour de Cassation de Côte d'Ivoire | [LinkedIn](https://www.linkedin.com/in/lioneldyla/)
