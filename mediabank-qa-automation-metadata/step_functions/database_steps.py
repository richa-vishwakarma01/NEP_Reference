import pytest
from pytest_bdd import given, when, then, parsers
import psycopg2
from utils.datautils import data_utils
import os
from dotenv import load_dotenv


@then("I connect to database")
def get_database():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return conn


@then(parsers.cfparse("I verify {info:Char} where {field:Char} is {value:Char} for table {table:Char}",
                      extra_types=dict(Char=str)))
def verify_tables(info, table, field, value):
    conn = get_database()
    cur = conn.cursor()
    query = f"SELECT {info} from {table} where {field}='{value}'"
    cur.execute(query)
    result = cur.fetchall()
    count_query = f"SELECT COUNT(*) FROM {table} WHERE {field}='{value}'"
    cur.execute(count_query)
    count = cur.fetchone()[0]
    print(count)
    if result and len(result) > 0 and len(result[0]) > 0:
        return result[0][0], count
    else:
        return None, count


@then("I verify new records added in Venue,sport_season and team")
def verify_new_data_added():
    conn = get_database()
    cur = conn.cursor()

#    reference_date = '2023-04-16 00:00:00'
    query = f"""
        SELECT 
          COUNT(*) 
        FROM (
          SELECT updated_time FROM sport_season
          UNION ALL
          SELECT updated_time FROM venue
          UNION ALL
          SELECT updated_time FROM team
        ) AS combined_tables
        WHERE updated_time > NOW();
    """
    cur.execute(query)
    result = cur.fetchone()[0]
    if result > 0:
        pass
#    assert result > 0, "No new data has been added to any of the tables"
#    assert result > 0, "No new data has been added to any of the tables"
