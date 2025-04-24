import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .utils import save_plot

sns.set_theme(style="whitegrid", context="notebook", palette="deep", 
             font_scale=1.2, rc={"figure.figsize": (10, 6)})

def plot_top_municipalities(df: pd.DataFrame, top_n: int = 10, save: bool = False) -> None:
    """Plots the top N municipalities with highest feminicide counts."""
    
    top_munis = df.head(top_n)
    
    ax = sns.barplot(
        data=top_munis, 
        x="victim_count", 
        y="municipality", 
        hue="municipality",
        legend=False,
        palette="Reds_r"
    )
    
    for i, v in enumerate(top_munis["victim_count"]):
        ax.text(v + 0.5, i, str(v), va='center')
    
    plt.title(f"Top {top_n} Municipalities with Highest Feminicide Cases (2018-2024)")
    plt.xlabel("Number of Feminicides")
    plt.ylabel("Municipality")
    
    sns.despine()
    plt.tight_layout()
    
    if save:
        save_plot(f"top_{top_n}_municipalities")
        
    
    plt.show()

def plot_trend_by_year(df: pd.DataFrame , save: bool = False) -> None:
    """
    Plots the trend of feminicide cases over the years.
    
    Args:
        df (pd.DataFrame): DataFrame grouped by year.
    """
    plt.figure(figsize=(12, 6))
    
    # Main plot
    ax = sns.lineplot(
        data=df, 
        x="year", 
        y="victim_count", 
        marker="o", 
        markersize=10,
        color="#8B0000", 
        linewidth=3
    )
    
    ax.fill_between(df["year"], df["victim_count"], alpha=0.2, color="#FF9999")
    
    for x, y in zip(df["year"], df["victim_count"]):
        ax.text(x, y + 2, str(y), ha='center', va='bottom', fontweight='bold')
    
    plt.title("Trend of Feminicides in Valle del Cauca (2018-2024)", 
              fontsize=16, pad=30)
    plt.xlabel("Year", fontsize=12, labelpad=15)
    plt.ylabel("Number of Feminicides", fontsize=12, labelpad=15)
    
    plt.xticks(df["year"])
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)
    
    ax.yaxis.grid(True, linestyle='-', alpha=0.3)
    ax.xaxis.grid(False)
    
    plt.tight_layout()
    
    if save:
        save_plot("trend_by_year") 
               
    plt.show()

def plot_by_subregion(df: pd.DataFrame, save: bool = False) -> None:
    """Plots total feminicides by subregion."""
    df_sorted = df.sort_values("victim_count", ascending=False)

    ax = sns.barplot(
        data=df_sorted, 
        x="victim_count", 
        y="subregion", 
        hue="subregion",
        legend=False,
        palette="magma"
    )
    
    for i, v in enumerate(df["victim_count"]):
        ax.text(v + 0.5, i, str(v), va='center')
    
    plt.title("Total Feminicides by Subregion (2018-2024)")
    plt.xlabel("Number of Feminicides")
    plt.ylabel("Subregion")
    
    sns.despine()
    plt.tight_layout()
    
    if save:
        save_plot("top_by_subregion")
            
    plt.show()

def plot_top_years(df: pd.DataFrame, top_n: int = 5, save: bool = False) -> None:
    """
    Creates a polished bar chart showing the top years with highest feminicide counts.
    
    Args:
        df (pd.DataFrame): DataFrame with years and victim counts, already sorted.
        top_n (int): Number of top years to display.
    """
    top_years = df.head(top_n)

    ax = sns.barplot(
        data=top_years, 
        x="year", 
        y="percentage", 
        hue="year",        
        palette="flare", 
        legend=False       
    )

    for i, v in enumerate(top_years["percentage"]):
        ax.text(i, v + 1, f"{v}%", ha='center', fontweight='bold')

    plt.title(f"Top {top_n} Years by % of Total Feminicides", pad=20)
    plt.xlabel("Year")
    plt.ylabel("Percentage of Total (%)")
    plt.tight_layout()
    
    if save:
        save_plot(f"top_{top_n}_municipalities")
        
    plt.show()
