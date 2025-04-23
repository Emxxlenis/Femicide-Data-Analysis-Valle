from src.load_data import load_data
from src.analysis import (get_feminicides_by_year, get_feminicides_by_municipality, get_feminicides_by_subregion, get_feminicides_trend  )
import os

if __name__ == "__main__":
    # Load raw data
    df_raw = load_data("data/raw/feminicides_valle_cauca_2020_2024_raw.xlsx")

    print(df_raw.head())
    # Run analysis
    yearly_stats = get_feminicides_by_year(df_raw)
    municipality_stats = get_feminicides_by_municipality(df_raw)
    subregion_stats = get_feminicides_by_subregion(df_raw)
    trend_stats = get_feminicides_trend(df_raw)
    # Print results
    print("\n📊 Feminicides by Year:")
    print(yearly_stats)
    print("\n📊 Feminicides by Municipality:")
    print(municipality_stats)
    print("\n📊 Feminicides by Subregion:")
    print(subregion_stats)
    print("\n📊 Feminicides Trend:")
    print(trend_stats)
