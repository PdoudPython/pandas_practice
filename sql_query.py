import sqlite3
import pandas as pd

DB_FILENAME = "netflix.db"          # or whichever dataset you're querying
CSV_SOURCE = "netflix_titles_clean.csv"   # ideally the cleaned data from the pandas project
TABLE_NAME = "netflix"


def create_connection(db_filename):
    """Create (or connect to) a SQLite database file."""
    # TODO: use sqlite3.connect(db_filename) and return the connection object
    pass


def load_csv_into_db(conn, csv_filename, table_name):
    """Read a CSV with pandas and write it into the SQLite database as a table."""
    # TODO: pd.read_csv() the source file
    # TODO: use df.to_sql(table_name, conn, if_exists='replace', index=False)
    pass


def run_query(conn, query):
    """Run a SQL query against the database and return the results."""
    # TODO: use pd.read_sql_query(query, conn) to get results as a DataFrame
    # return the result
    pass


def main():
    conn = create_connection(DB_FILENAME)
    load_csv_into_db(conn, CSV_SOURCE, TABLE_NAME)

    # TODO: write a handful of business questions as SQL queries and run them, e.g.:
    #   - How many titles are Movies vs TV Shows?
    #   - Which country has produced the most titles?
    #   - What are the top 5 most common genres/categories?
    #   - How has the number of titles added to Netflix changed by year?
    #   - Which director/cast member appears most often?
    #
    # example:
    # query = "SELECT type, COUNT(*) FROM netflix GROUP BY type;"
    # result = run_query(conn, query)
    # print(result)

    conn.close()


if __name__ == "__main__":
    main()
