import pandas as pd

FILENAME = "data/netflix_titles.csv"          # adjust path if needed
OUTPUT_FILENAME = "netflix_titles_clean.csv"


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


def fix_data_types(df):
    """Correct columns that aren't in a useful type (e.g. dates stored as strings)."""
    # TODO: look at df.dtypes - which columns should be datetime, int, category, etc.?
    # TODO: use pd.to_datetime() on any date columns
    # return the modified DataFrame
    pass


def standardize_text_columns(df):
    """Clean up inconsistent text formatting (casing, whitespace, etc.)."""
    # TODO: pick a column or two (e.g. 'country', 'rating') and check for inconsistent values
    #   - hint: df['column'].unique() or .value_counts() will show you what's actually in there
    # TODO: use .str.strip(), .str.title(), or similar as needed
    # return the modified DataFrame
    pass


def save_clean_data(df, filename):
    """Save the cleaned DataFrame to a new CSV file."""
    # TODO: use df.to_csv(filename, index=False)
    pass


def main():
    df = load_data(FILENAME)
    inspect_data(df)

    # TODO: call your cleaning functions in a sensible order
    # df = handle_missing_values(df)
    # df = handle_duplicates(df)
    # df = fix_data_types(df)
    # df = standardize_text_columns(df)

    # TODO: inspect again after cleaning to confirm it worked
    # inspect_data(df)

    # save_clean_data(df, OUTPUT_FILENAME)


if __name__ == "__main__":
    main()
