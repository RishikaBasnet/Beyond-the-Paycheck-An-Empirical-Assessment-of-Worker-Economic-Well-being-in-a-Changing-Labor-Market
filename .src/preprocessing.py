import pandas as pd

from data_cleaning import load_raw_data

yes_no_map = {"Yes": 100, "No": 0}
no_yes_map = {"Yes": 0, "No": 100}

d30_map = {
    "Schedule varies at my request": 100,
    "Normally work same hours": 50,
    "Schedule varies based on employer needs": 0,
}

d28_b_map = {
    "Never": 0,
    "Rarely": 25,
    "Sometimes": 50,
    "Often": 75,
    "Always": 100,
}

b2_map = {
    "Finding it difficult to get by": 0,
    "Just getting by": 33,
    "Doing okay": 67,
    "Living comfortably": 100,
}

i9_map = {
    "Varies quite often from month to month": 0,
    "Occasionally varies from month to month": 50,
    "Roughly the same amount each month": 100,
}


def build_clean_df(df):
    clean_df = pd.DataFrame()

    clean_df["Access to Benefits"] = pd.concat([
        df["E4_a"].map(yes_no_map),
        df["K21_b"].map(yes_no_map),
    ], axis=1).mean(axis=1)

    clean_df["Income Stability"] = df["I9"].map(i9_map)

    clean_df["Job Flexibility"] = pd.concat([
        df["D30"].map(d30_map),
        df["D28_a"].map(yes_no_map),
        df["D28_b"].map(d28_b_map),
    ], axis=1).mean(axis=1)

    clean_df["Financial Resilience"] = pd.concat([
        df["EF1"].map(yes_no_map),
        df["EF2"].map(yes_no_map),
        df["B2"].map(b2_map),
    ], axis=1).mean(axis=1)

    clean_df["Income Adequacy"] = df["I12"].map(no_yes_map)

    return clean_df


if __name__ == "__main__":
    df = load_raw_data()
    clean_df = build_clean_df(df)
    print(clean_df.head())
