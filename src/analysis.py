"""
Analysis functions for the feminicide dataset in Valle del Cauca (2020–2024).

"""

import pandas as pd

def get_feminicides_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with the total number of feminicides per year.

    Args:
        df (pd.DataFrame): The cleaned dataset.

    Returns:
        pd.DataFrame: A DataFrame grouped by year, sorted in descending order.
    """
    grouped = df.groupby("year", as_index=False)["victim_count"].sum()
    return grouped.sort_values(by="victim_count", ascending=False)


def get_feminicides_by_municipality(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with the total number of feminicides per municipality.

    Args:
        df (pd.DataFrame): The cleaned dataset.

    Returns:
        pd.DataFrame: A DataFrame grouped by municipality, sorted in descending order.
    """
    grouped = df.groupby("municipality", as_index=False)["victim_count"].sum()
    return grouped.sort_values(by="victim_count", ascending=False)


def get_feminicides_by_subregion(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with the total number of feminicides per subregion.

    Args:
        df (pd.DataFrame): The cleaned dataset.

    Returns:
        pd.DataFrame: A DataFrame grouped by subregion, sorted in descending order.
    """
    grouped= df.groupby("subregion", as_index=False)["victim_count"].sum()
    return grouped.sort_values(by="victim_count", ascending=False)


def get_feminicides_trend(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame showing the trend of feminicides over time (by year), 
    including the percentage of total cases per year.

    Args:
        df (pd.DataFrame): The cleaned dataset.

    Returns:
        pd.DataFrame: A DataFrame with year, victim count, and percentage.
    """
    grouped = df.groupby("year", as_index=False)["victim_count"].sum()
    total = grouped["victim_count"].sum()
    grouped["percentage"] = round((grouped["victim_count"] / total) * 100, 2)
    return grouped

