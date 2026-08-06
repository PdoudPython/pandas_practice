import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

# TODO: fill in your actual Postgres connection details
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
    # TODO: use psycopg2.connect(**config) and return the connection object
    try:
        conn = psycopg2.connect(**config)
    except psycopg2.OperationalError as e:
        print(f"Database connection failed: {e}")
        conn = None
    return conn

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


def main():
    conn = create_connection(DB_CONFIG)
    create_netflix_table(conn)
    load_csv_into_db(conn, CSV_SOURCE)

    movies_and_shows = """
        SELECT type, COUNT(*) 
        FROM netflix 
        GROUP BY type;
    """
    result = run_query(conn, movies_and_shows)
    print(result)

    title_by_country = """
        SELECT country, COUNT(*) as title_count 
        FROM netflix 
        GROUP BY country 
        ORDER BY title_count DESC;
    """
    result = run_query(conn, title_by_country)
    print(result)

    most_common_genre = """
        SELECT listed_in, COUNT(*) as most_common
        FROM netflix 
        GROUP BY listed_in 
        ORDER BY most_common DESC;
    """
    result = run_query(conn, most_common_genre)
    print(result)

    titles_per_year = """
        SELECT EXTRACT(YEAR FROM date_added) as year_added, COUNT(*) as title_per_year
        FROM netflix 
        GROUP BY year_added
        ORDER BY title_per_year DESC;
    """
    result = run_query(conn, titles_per_year)
    print(result)

    common_director_and_cast = """
        SELECT director, show_cast, COUNT(*) as production
        FROM netflix 
        WHERE director != 'NOT LISTED' and show_cast != 'NOT LISTED'
        GROUP BY director, show_cast
        ORDER BY production DESC
        LIMIT 5;
    """
    result = run_query(conn, common_director_and_cast)
    print(result)
    conn.close()


if __name__ == "__main__":
    main()