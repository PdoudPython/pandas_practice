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

def standardize_text_columns(df):
    """Clean up inconsistent text formatting (casing, whitespace, etc.)."""
    # TODO: pick a column or two (e.g. 'country', 'rating') and check for inconsistent values
    #   - hint: df['column'].unique() or .value_counts() will show you what's actually in there
    # TODO: use .str.strip(), .str.title(), or similar as needed
    # return the modified DataFrame
    print(df['country'].value_counts())
    print(df['rating'].value_counts())
    wrong_rows = df[df['rating'].isin(['74 min', '84 min', '66 min'])].index
    df.loc[wrong_rows, 'duration'] = df.loc[wrong_rows, 'rating']
    

loaded_file = load_data(FILENAME)
inspect_data(loaded_file)
standardize_text_columns(loaded_file)
print(loaded_file[loaded_file['rating'].isin(['74 min', '84 min', '66 min'])])