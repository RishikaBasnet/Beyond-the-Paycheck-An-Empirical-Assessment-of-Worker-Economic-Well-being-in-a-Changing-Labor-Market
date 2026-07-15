import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data_cleaning import load_raw_data
from preprocessing import build_clean_df
from scoring import esi_weights, add_economic_security_index


def plot_dimension_averages(clean_df):
    # Plots average for the entire sample of individuals of every dimension considered
    dimension_averages = clean_df.drop(columns=["Economic Security Index"]).mean().sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))
    dimension_averages.plot(kind="barh", ax=ax, color="#4C72B0")
    ax.set_xlabel("Average Score (0-100)")
    ax.set_title("Average Score by Dimension (All Respondents)")
    ax.set_xlim(0, 100)
    plt.tight_layout()

    output_path = "Figures/dimension_averages.png"
    plt.savefig(output_path, dpi=300)
    print(f"Saved bar chart to {output_path}")


def plot_dimension_weights():
  # Plots the weight of each dimension in calculating the economic security index
    weights = pd.Series(esi_weights).sort_values() * 100

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(weights.index, weights.values, color="#55A868")
    ax.set_xlabel("Weight in Economic Security Index (%)")
    ax.set_title("Dimension Weights in Economic Security Index")
    ax.set_xlim(0, 100)
    ax.bar_label(bars, fmt="%.1f%%", padding=3)
    plt.tight_layout()

    output_path = "Figures/economic_security_index_weights.png"
    plt.savefig(output_path, dpi=300)
    print(f"Saved bar chart to {output_path}")


def plot_economic_security_index_histogram(clean_df):
  #Plots the economic security index for each individual in the sample population surveryed
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(clean_df["Economic Security Index"].dropna(), bins=20, color="#C44E52", edgecolor="white")
    ax.set_xlabel("Economic Security Index (0-100)")
    ax.set_ylabel("Number of Participants")
    ax.set_title("Distribution of Economic Security Index (All Respondents)")
    ax.set_xlim(0, 100)
    plt.tight_layout()

    output_path = "Figures/economic_security_index_histogram.png"
    plt.savefig(output_path, dpi=300)
    print(f"Saved histogram to {output_path}")


def plot_flexibility_vs_economic_security_index(clean_df):
  # Plots the relationship of the flexibility and economic security index
    scatter_df = clean_df[["Job Flexibility", "Economic Security Index"]].dropna()

    slope, intercept = np.polyfit(scatter_df["Job Flexibility"], scatter_df["Economic Security Index"], 1)
    trend_x = np.array([0, 100])
    trend_y = slope * trend_x + intercept

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(scatter_df["Job Flexibility"], scatter_df["Economic Security Index"], alpha=0.4, color="#4C72B0", edgecolor="none")
    ax.plot(trend_x, trend_y, color="#C44E52", linewidth=2, label=f"Trend (slope = {slope:.2f})")
    ax.set_xlabel("Job Flexibility (0-100)")
    ax.set_ylabel("Economic Security Index (0-100)")
    ax.set_title("Job Flexibility vs. Economic Security Index (All Respondents)")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.legend()
    plt.tight_layout()

    output_path = "Figures/flexibility_vs_economic_security_index.png"
    plt.savefig(output_path, dpi=300)
    print(f"Saved scatter plot to {output_path}")


if __name__ == "__main__":
    df = load_raw_data()
    clean_df = build_clean_df(df)
    clean_df = add_economic_security_index(clean_df)

    plot_dimension_averages(clean_df)
    plot_dimension_weights()
    plot_economic_security_index_histogram(clean_df)
    plot_flexibility_vs_economic_security_index(clean_df)
