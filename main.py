from src.load_data import load_data
from src.analysis import (
    get_feminicides_by_year,
    get_feminicides_by_municipality,
    get_feminicides_by_subregion,
    get_feminicides_trend
)
from src.plotting import (
    plot_top_municipalities,
    plot_trend_by_year,
    plot_by_subregion,
    plot_top_years
)
from src.utils import save_dataframe

# --- Config ---
RAW_PATH = "data/raw/feminicides_valle_cauca_2020_2024_raw.xlsx"

if __name__ == "__main__":
    # --- Load data ---
    df_raw = load_data(RAW_PATH)
    print("✅ Raw data loaded. Preview:")
    print(df_raw.head())

    # --- Run Analysis ---
    municipality_stats = get_feminicides_by_municipality(df_raw)
    subregion_stats = get_feminicides_by_subregion(df_raw)
    trend_df = get_feminicides_trend(df_raw)
    feminicides_year = get_feminicides_by_year(df_raw)

    # --- Save results ---
    save_dataframe(municipality_stats, "feminicides_by_municipality")
    save_dataframe(subregion_stats, "feminicides_by_subregion")
    save_dataframe(trend_df, "feminicides_trend")
    save_dataframe(feminicides_year, "feminicides_by_year")

    print("✅ Data analysis complete and saved to /data/processed")

    # --- Visualizations ---
    plot_top_municipalities(municipality_stats, save=True)
    plot_trend_by_year(feminicides_year, save=True)
    plot_by_subregion(subregion_stats, save=True)
    plot_top_years(trend_df, save=True)

    print("✅ All plots generated and saved to /outputs/plots")

    # --- Optional Console Output ---
    """
    print("\n📊 Feminicides by Year:")
    print(feminicides_year)
    print("\n📊 Feminicides by Municipality:")
    print(municipality_stats)
    print("\n📊 Feminicides by Subregion:")
    print(subregion_stats)
    print("\n📊 Feminicides Trend:")
    print(trend_df)
    """
