import pandas as pd

FILENAME = "data/netflix_titles.csv"          # adjust path if needed
OUTPUT_FILENAME = "data/netflix_titles_clean.csv"


def load_data(filename):
    """Load the raw CSV into a DataFrame."""
    data_load = pd.read_csv(filename)
    return data_load


def inspect_data(df):
    """Print out useful information to understand the dataset before cleaning."""
    print(df.info())
    print(df.isnull().sum())
    print(df.describe(include='all'))
    print(df.duplicated().sum())

def handle_missing_values(df):
    """Decide what to do with missing values in each column."""
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()
    df= df.fillna({
        'director': 'NOT LISTED',
        'cast': 'NOT LISTED',
        'country': 'NOT LISTED',
        'rating': 'No Rating'
        })
    df = df.dropna(subset=['date_added', 'duration'])
    return df


def handle_duplicates(df):
    """Remove duplicate rows, if any exist."""
    df = df.drop_duplicates()
    return df


def fix_data_types(df):
    """Correct columns that aren't in a useful type (e.g. dates stored as strings)."""
    print(df.dtypes)
    df['date_added'] = df['date_added'].apply(pd.to_datetime)
    return df

def standardize_text_columns(df):
    print(df['country'].value_counts())
    print(df['rating'].value_counts())
    wrong_rows = df[df['rating'].isin(['74 min', '84 min', '66 min'])].index
    df.loc[wrong_rows, 'duration'] = df.loc[wrong_rows, 'rating']
    df = df.replace({'rating': {'74 min': 'No Rating', '84 min': 'No Rating', '66 min': 'No Rating'}})
    return df

def save_clean_data(df, filename):
    """Save the cleaned DataFrame to a new CSV file."""
    df.to_csv(filename, index=False)


def main():
    df = load_data(FILENAME)
    inspect_data(df)

    # TODO: call your cleaning functions in a sensible order
    df = standardize_text_columns(df)
    df = handle_missing_values(df)
    df = handle_duplicates(df)
    df = fix_data_types(df)
    

    # TODO: inspect again after cleaning to confirm it worked
    inspect_data(df)

    save_clean_data(df, OUTPUT_FILENAME)


if __name__ == "__main__":
    main()
