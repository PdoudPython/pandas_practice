import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "netflix_db",
    "user": "postgres",
    "password": "postgres",
}

CSV_SOURCE = "data/netflix_titles_clean.csv"   # the cleaned data from the pandas project
TABLE_NAME = "netflix"


def create_connection(config):
    """Create a connection to the Postgres database."""
    try:
        conn = psycopg2.connect(**config)
    except psycopg2.OperationalError as e:
        print(f"Database connection failed: {e}")
        conn = None
    return conn

def get_db_connection():
    return create_connection(DB_CONFIG)

def create_netflix_table(conn):
    """Create the netflix table if it doesn't already exist."""
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS netflix(
        show_id VARCHAR(10) PRIMARY KEY,
        type TEXT,
        title TEXT,
        director TEXT,
        show_cast TEXT,
        country TEXT,
        date_added DATE,
        release_year INTEGER,
        rating VARCHAR,
        duration TEXT,
        listed_in VARCHAR(100),
        description TEXT
    );"""
    )
    conn.commit()


def load_csv_into_db(conn, csv_filename):
    """Read the cleaned CSV with pandas and bulk-insert it into the Postgres table."""

    df = pd.read_csv(csv_filename)
    df_tuples = df.values.tolist()

    insert_query = """
        INSERT INTO netflix (show_id, type, title, director, show_cast, country, date_added, release_year, rating, duration, listed_in, description)
        VALUES %s
        ON CONFLICT (show_id) DO NOTHING
    """
    cur = conn.cursor()
    execute_values(cur, insert_query, df_tuples)

    conn.commit()


def run_query(conn, query):
    """Run a SQL query against the database and return the results."""
    df = pd.read_sql_query(query, conn)
    return df


def get_type_distribution(conn):
    """Count of Movies vs TV Shows."""
    query = """
        SELECT type, COUNT(*) as type_count
        FROM netflix 
        GROUP BY type;
    """
    return run_query(conn, query)


def get_titles_by_country(conn, limit=None):
    """Count of titles per country, ranked descending. Optionally limited to top N."""
    query = """
        SELECT country, COUNT(*) as title_count 
        FROM netflix 
        GROUP BY country 
        ORDER BY title_count DESC
    """
    if limit is not None:
        query += f" LIMIT {limit};"
    else:
        query += ";"
    return run_query(conn, query)


def get_genre_distribution(conn):
    """Count of titles per genre, ranked descending."""
    query = """
        SELECT listed_in, COUNT(*) as genre_count
        FROM netflix 
        GROUP BY listed_in 
        ORDER BY genre_count DESC;
    """
    return run_query(conn, query)


def get_titles_by_year(conn):
    """Count of titles added per year."""
    query = """
        SELECT EXTRACT(YEAR FROM date_added) as year_added, COUNT(*) as title_count
        FROM netflix 
        GROUP BY year_added
        ORDER BY year_added;
    """
    return run_query(conn, query)


def get_top_director_cast_pairs(conn, limit=5):
    """Most frequent director/cast pairings, excluding unlisted values."""
    query = f"""
        SELECT director, show_cast, COUNT(*) as production
        FROM netflix 
        WHERE director != 'NOT LISTED' and show_cast != 'NOT LISTED'
        GROUP BY director, show_cast
        ORDER BY production DESC
        LIMIT {limit};
    """
    return run_query(conn, query)


def main():
    conn = create_connection(DB_CONFIG)
    create_netflix_table(conn)
    load_csv_into_db(conn, CSV_SOURCE)

    type_distribution = get_type_distribution(conn)
    print(type_distribution)

    titles_by_country = get_titles_by_country(conn, limit=None)
    print(titles_by_country)

    genre_distribution = get_genre_distribution(conn)
    print(genre_distribution)

    titles_by_year = get_titles_by_year(conn)
    print(titles_by_year)

    top_director_cast_pairs = get_top_director_cast_pairs(conn, limit=5)
    print(top_director_cast_pairs)

    conn.close()


if __name__ == "__main__":
    main()