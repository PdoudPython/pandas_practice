import pandas as pd

FILENAME = "data/netflix_titles.csv"          # adjust path if needed
OUTPUT_FILENAME = "netflix_titles_clean.csv"


def load_data(filename):
    """Load the raw CSV into a DataFrame."""
    data_load = pd.read_csv(filename)
    return data_load

def inspect_data(df):
    """Print out useful information to understand the dataset before cleaning."""
    # TODO: call df.info()
    # TODO: call df.isnull().sum()
    # TODO: call df.describe(include='all') or df.head() if useful
    # TODO: check for duplicate rows with df.duplicated().sum()
    print(df.info())
    print(df.isnull().sum())
    print(df.describe(include='all'))
    print(df.duplicated().sum())

loaded_file = load_data(FILENAME)
inspect_data(loaded_file)