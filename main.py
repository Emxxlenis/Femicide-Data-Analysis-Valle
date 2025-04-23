from src.load_data import load_data

if __name__ == "__main__":
    # Load raw data
    df_raw = load_data("data/raw/feminicides_valle_cauca_2020_2024_raw.xlsx")

    print(df_raw.head())
 