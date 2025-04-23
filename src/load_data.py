import pandas as pd
import os

def load_data(file_path: str):
    """
    Load data from a .xlsx file 

    Args:
        file_path (str): The path to the .xlsx file.

    Returns:
    DataFrame: A pandas DataFrame containing the data from the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Load the data from the .xlsx file
    df = pd.read_excel(file_path)
    df.rename(columns={
        'Año': 'year',
        'Id_municipio': 'municipality_id',
        'Municipio': 'municipality',
        'Subregión': 'subregion',
        'Cantidad': 'victim_count'
    }, inplace=True)   
    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns from {file_path}.")
    return df



