import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "netflix_titles_clean.csv"   # use your cleaned dataset from the pandas project


def load_data(filename):
    """Load the cleaned CSV into a DataFrame."""
    # TODO: use pd.read_csv() and return the DataFrame
    pass


def plot_type_distribution(df):
    """Bar chart: count of Movies vs TV Shows."""
    # TODO: use df['type'].value_counts()
    # TODO: plot with .plot(kind='bar') or plt.bar()
    # TODO: add a title, xlabel, ylabel
    # TODO: plt.show()
    pass


def plot_titles_over_time(df):
    """Line chart: number of titles added per year."""
    # TODO: you'll need a proper datetime column (from the cleaning project) to extract year
    # TODO: group by year and count titles, then plot as a line chart
    pass


def plot_top_countries(df):
    """Bar chart: top N countries by number of titles produced."""
    # TODO: some rows may have multiple countries listed (comma-separated) - think about
    #   whether you want to split those out or just count the raw string as-is
    # TODO: use value_counts() on the country column, take the top N with .head(N)
    # TODO: plot as a horizontal or vertical bar chart
    pass


def plot_rating_distribution(df):
    """Bar chart: distribution of content ratings (e.g. PG, TV-MA, etc.)."""
    # TODO: similar approach to plot_type_distribution but for the 'rating' column
    pass


def main():
    df = load_data(FILENAME)

    # TODO: call each plotting function
    # plot_type_distribution(df)
    # plot_titles_over_time(df)
    # plot_top_countries(df)
    # plot_rating_distribution(df)


if __name__ == "__main__":
    main()
