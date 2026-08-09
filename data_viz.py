import matplotlib.pyplot as plt
import pandas as pd
from sql_query import get_type_distribution, get_titles_by_country, get_genre_distribution, get_titles_by_year, get_top_director_cast_pairs, get_db_connection


def plot_type_distribution(conn):
    """Bar chart: count of Movies vs TV Shows."""
    df = get_type_distribution(conn)

    df.plot(kind='bar', x='type', y='type_count')
    plt.title('Movies vs TV Shows Type Distribution')
    plt.xlabel('Movies vs TV Shows')
    plt.ylabel('Count')
    plt.show()



def plot_titles_by_year(conn):
    """Line chart: number of titles added per year."""
    df = get_titles_by_year(conn)

    df.plot(kind='line', x='year_added', y='title_count')
    plt.title('Number of Titles Added to Netflix Each Year')
    plt.xlabel('Year Added to Netflix')
    plt.ylabel('Number of Titles Added')
    plt.show()

def plot_top_countries(conn):
    """Bar chart: top N countries by number of titles produced."""
    df = get_titles_by_country(conn, limit=10)

    df.plot(kind='barh', x='country', y='title_count')
    plt.title('Number of Titles Per Country')
    plt.xlabel('Number of Titles')
    plt.ylabel('Country')
    plt.show()


def plot_director_cast_pairs(conn):
    """Bar chart: most frequent director/cast pairings."""
    df = get_top_director_cast_pairs(conn, limit=5)

    df['pair'] = df['director'] + ' w/\n ' + df['show_cast'].str.replace(', ', '\n')

    df.plot(kind='barh', x='pair', y='production')
    plt.title('Most Frequent Director/Cast Pairings')
    plt.xlabel('Number of Times Paired')
    plt.ylabel('Director and Cast Member')
    plt.show()



def main():
    conn = get_db_connection()

    plot_type_distribution(conn)
    plot_titles_by_year(conn)
    plot_top_countries(conn)
    plot_director_cast_pairs(conn)

    conn.close()

if __name__ == "__main__":
    main()