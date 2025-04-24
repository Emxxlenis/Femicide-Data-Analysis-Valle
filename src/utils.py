import os
import pandas as pd
import matplotlib.pyplot as plt


def save_dataframe(df: pd.DataFrame, filename: str, folder: str = "data/processed") -> None:
    """
    Saves the given DataFrame to a CSV file in the specified folder.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        filename (str): Name of the output file (without extension).
        folder (str): Target folder to save the CSV file.
    """
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{filename}.csv")
    df.to_csv(filepath, index=False)
    print(f"Saved to {filepath}")


def save_plot(filename: str, folder: str = "outputs/plots") -> None:
    """
    Saves the current matplotlib plot to a PNG file.

    Args:
        filename (str): Name of the file to save (without extension).
        folder (str): Folder path to save the file.
    """
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{filename}.png")
    plt.savefig(path, bbox_inches="tight")
    print(f"Plot saved to {path}")