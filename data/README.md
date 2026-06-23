# Data Directory

This directory contains all data files for the **Judicial Statistics — Côte d'Ivoire** project.

> **Note:** Raw data files are not versioned in this repository due to confidentiality constraints of the Ministry of Justice. Only the data structure, schema, and processed outputs are documented here.

## Directory Structure

```
data/
├── raw/              # Original source data (not committed — see .gitignore)
│   ├── 2019/         # Annuaire Statistique Judiciaire 2019
│   └── 2023/         # Annuaire Statistique Judiciaire et Pénitentiaire 2023
├── processed/        # Cleaned and structured datasets (CSV/Excel)
│   ├── cases_by_jurisdiction_2019.csv
│   ├── cases_by_jurisdiction_2023.csv
│   ├── clearance_rates_2019_2023.csv
│   ├── backlog_evolution.csv
│   └── penitentiary_2023.csv
└── README.md         # This file
```

## Data Sources

| Publication | Year | Publisher | Scope |
|---|---|---|---|
| Annuaire Statistique Judiciaire | 2019 | Direction des Affaires Civiles et Pénales, Ministère de la Justice | Civil, criminal, and commercial courts |
| Annuaire Statistique Judiciaire et Pénitentiaire | 2023 | Direction de la Planification, Ministère de la Justice | Courts + penitentiary system |

## Key Variables

### Case Data (Affaires judiciaires)

| Variable | Description | Unit |
|---|---|---|
| `juridiction` | Court name | String |
| `annee` | Reference year | Integer |
| `affaires_entrees` | Cases filed (incoming) | Count |
| `affaires_jugees` | Cases adjudicated | Count |
| `affaires_en_stock` | Cases pending (backlog) | Count |
| `taux_clearance` | Clearance rate (jugées/entrées) | Percentage |
| `taux_engorgement` | Backlog ratio | Percentage |

### Court Levels

| Code | Level | French Name |
|---|---|---|
| `TGI` | Court of First Instance | Tribunal de Grande Instance |
| `CA` | Court of Appeal | Cour d'Appel |
| `COUR_CASS` | Court of Cassation | Cour de Cassation |
| `TPI` | Court of First Instance (minor) | Tribunal de Première Instance |
| `TA` | Administrative Court | Tribunal Administratif |

### Penitentiary Data (2023 only)

| Variable | Description | Unit |
|---|---|---|
| `etablissement` | Prison facility name | String |
| `capacite` | Designed capacity | Count |
| `population_carcerale` | Actual prison population | Count |
| `taux_occupation` | Occupancy rate | Percentage |
| `preventifs` | Pre-trial detainees | Count |
| `condamnes` | Convicted inmates | Count |

## Data Pipeline

1. **Extraction** — Manual extraction from PDF yearbooks into Excel
2. **Cleaning** — Standardization of court names, year labels, and numeric formats via `analysis/eda_judicial_stats.py`
3. **Transformation** — Computation of derived indicators (clearance rate, backlog index)
4. **Output** — Structured CSV files stored in `data/processed/`

## Contact

For data access inquiries, contact: [Lionel Dyla on LinkedIn](https://www.linkedin.com/in/lioneldyla/)
