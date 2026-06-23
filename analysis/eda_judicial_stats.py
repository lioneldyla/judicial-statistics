"""
Judicial Statistics — Exploratory Data Analysis
================================================
Author: Yoboukoua DJORO | Ministry of Justice, Côte d'Ivoire
LinkedIn: https://www.linkedin.com/in/lioneldyla/
GitHub: https://github.com/lioneldyla/judicial-statistics

Description:
    This script performs exploratory data analysis (EDA) on judicial
    statistics data from the national Yearbooks (2019, 2023).
    It computes key indicators, trends, and visualizations to support
    evidence-based judicial policy and reform.

Data sources:
    - Judicial Statistics Yearbook 2019, Ministry of Justice, Côte d'Ivoire
    - Judicial and Penitentiary Statistics Yearbook 2023, Directorate of Planning
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

COURT_TYPES = [
    "Tribunal de Première Instance (TPI)",
    "Tribunal de Commerce",
    "Cour d'Appel",
    "Cour de Cassation",
    "Tribunal Militaire",
]

CASE_CATEGORIES = [
    "Pénal",
    "Civil",
    "Commercial",
    "Administratif",
    "Famille",
]


# ============================================================
# Data Loading
# ============================================================

def load_judicial_data(filepath: str) -> pd.DataFrame:
    """
    Load judicial statistics from CSV file.
    Expected columns: year, court, category, cases_filed, cases_closed, pending
    """
    df = pd.read_csv(filepath)
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["cases_filed"] = pd.to_numeric(df["cases_filed"], errors="coerce")
    df["cases_closed"] = pd.to_numeric(df["cases_closed"], errors="coerce")
    df["pending"] = pd.to_numeric(df["pending"], errors="coerce")
    return df


# ============================================================
# Key Indicators
# ============================================================

def compute_clearance_rate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Case Clearance Rate = (Cases Closed / Cases Filed) * 100
    Measures court efficiency: how many filed cases are resolved.
    """
    df = df.copy()
    df["clearance_rate"] = (df["cases_closed"] / df["cases_filed"] * 100).round(2)
    return df


def compute_backlog_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Backlog Index = Pending Cases / Cases Filed
    Values > 1 indicate growing backlog; < 1 indicates improvement.
    """
    df = df.copy()
    df["backlog_index"] = (df["pending"] / df["cases_filed"]).round(3)
    return df


def compute_processing_efficiency(df: pd.DataFrame) -> pd.DataFrame:
    """Compute both clearance rate and backlog index."""
    df = compute_clearance_rate(df)
    df = compute_backlog_index(df)
    return df


# ============================================================
# Analysis Functions
# ============================================================

def summary_by_court(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate key metrics by court type."""
    return df.groupby("court").agg(
        total_filed=("cases_filed", "sum"),
        total_closed=("cases_closed", "sum"),
        avg_clearance_rate=("clearance_rate", "mean"),
        avg_backlog_index=("backlog_index", "mean"),
    ).round(2).sort_values("total_filed", ascending=False)


def summary_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate key metrics by case category."""
    return df.groupby("category").agg(
        total_filed=("cases_filed", "sum"),
        total_closed=("cases_closed", "sum"),
        avg_clearance_rate=("clearance_rate", "mean"),
    ).round(2).sort_values("total_filed", ascending=False)


def trend_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """Year-over-year trend of filed and closed cases."""
    return df.groupby("year").agg(
        total_filed=("cases_filed", "sum"),
        total_closed=("cases_closed", "sum"),
        total_pending=("pending", "sum"),
        avg_clearance_rate=("clearance_rate", "mean"),
    ).round(2)


# ============================================================
# Visualization
# ============================================================

def plot_clearance_by_court(df: pd.DataFrame, output_path: Path = None):
    """Bar chart: average clearance rate by court type."""
    summary = summary_by_court(df)[["avg_clearance_rate"]].reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["#2196F3" if r >= 80 else "#FF9800" if r >= 60 else "#F44336"
              for r in summary["avg_clearance_rate"]]
    bars = ax.barh(summary["court"], summary["avg_clearance_rate"], color=colors)
    ax.axvline(80, color="green", linestyle="--", linewidth=1.5, label="Target: 80%")
    ax.set_xlabel("Clearance Rate (%)")
    ax.set_title("Case Clearance Rate by Court Type\nCôte d'Ivoire Judicial Statistics")
    ax.legend()
    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=150, bbox_inches="tight")
    return fig


def plot_annual_trend(df: pd.DataFrame, output_path: Path = None):
    """Line chart: annual evolution of filed vs closed cases."""
    trend = trend_by_year(df).reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(trend["year"], trend["total_filed"], marker="o", label="Cases Filed", linewidth=2)
    ax.plot(trend["year"], trend["total_closed"], marker="s", label="Cases Closed", linewidth=2)
    ax.fill_between(trend["year"],
                    trend["total_closed"],
                    trend["total_filed"],
                    alpha=0.15, label="Gap (Backlog)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Cases")
    ax.set_title("Annual Trend: Cases Filed vs Closed\nCôte d'Ivoire Judicial Statistics")
    ax.legend()
    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=150, bbox_inches="tight")
    return fig


# ============================================================
# Main Execution
# ============================================================

def run_eda(filepath: str):
    """Run the full EDA pipeline."""
    print("=" * 60)
    print("JUDICIAL STATISTICS — EXPLORATORY DATA ANALYSIS")
    print("Côte d'Ivoire | Ministry of Justice")
    print("=" * 60)

    # Load and preprocess
    df = load_judicial_data(filepath)
    df = compute_processing_efficiency(df)

    print(f"\n Dataset: {len(df)} records | Years: {df['year'].min()}–{df['year'].max()}")
    print(f" Courts covered: {df['court'].nunique()}")
    print(f" Case categories: {df['category'].nunique()}")

    # Summary tables
    print("\n--- Summary by Court ---")
    print(summary_by_court(df).to_string())

    print("\n--- Summary by Case Category ---")
    print(summary_by_category(df).to_string())

    print("\n--- Annual Trend ---")
    print(trend_by_year(df).to_string())

    # Visualizations
    plot_clearance_by_court(df, OUTPUT_DIR / "clearance_by_court.png")
    plot_annual_trend(df, OUTPUT_DIR / "annual_trend.png")

    print(f"\n Visualizations saved to: {OUTPUT_DIR}/")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    filepath = sys.argv[1] if len(sys.argv) > 1 else DATA_DIR / "judicial_stats_sample.csv"
    run_eda(filepath)
