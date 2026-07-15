from data_cleaning import load_raw_data
from preprocessing import build_clean_df

esi_weights = {
    "Access to Benefits": 0.138,
    "Income Stability": 0.112,
    "Job Flexibility": 0.138,
    "Financial Resilience": 0.112,
    "Income Adequacy": 0.50,
}


def add_economic_security_index(clean_df):
    clean_df["Economic Security Index"] = sum(
        weight * clean_df[dimension] for dimension, weight in esi_weights.items()
    )
    return clean_df


if __name__ == "__main__":
    df = load_raw_data()
    clean_df = build_clean_df(df)
    clean_df = add_economic_security_index(clean_df)

    print(clean_df.head())
    print("Average Economic Security Index:", clean_df["Economic Security Index"].mean())
    print(
        "Respondents with a valid Economic Security Index:",
        clean_df["Economic Security Index"].notna().sum(),
        "/",
        len(clean_df),
    )
