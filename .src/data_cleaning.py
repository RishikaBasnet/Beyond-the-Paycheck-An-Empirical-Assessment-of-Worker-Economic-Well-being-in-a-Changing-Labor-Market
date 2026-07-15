import pandas as pd
from numbers_parser import Document


def load_raw_data(path="data/raw/SHED (financial security)/public2025.numbers"):
    doc = Document(path)
    tables = doc.sheets[0].tables
    data = tables[0].rows(values_only=True)
    return pd.DataFrame(data[1:], columns=data[0])


if __name__ == "__main__":
    df = load_raw_data()
    print(df.head())
    print(df.columns)
