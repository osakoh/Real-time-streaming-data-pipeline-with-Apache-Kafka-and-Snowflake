import os
import sys

from snowflake.connector import connect
from snowflake.connector import errors


def create_db_connection():
    """ function to establish a database connection """
    conn = None
    try:
        conn = connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_ACCOUNT"),
            account=os.getenv("SNOWFLAKE_PASSWORD"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            role=os.getenv("SNOWFLAKE_ROLE"),
            session_parameters={
                'TIMEZONE': 'UTC',
            }
        )
    except (KeyError, errors.ProgrammingError) as e:
        sys.exit(f"Exiting script.........{e}")
    return conn


def create_db(conn):
    """
    :param conn: database connection

    Creates a new database in Snowflake
    """
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE DATABASE IF NOT EXISTS shop_db""")
        conn.commit()
        cursor.close()
        print("shop_db created successfully.\n")

    except Exception as e:
        print(f"Error: {e}\n")
        conn.rollback()
        cursor.close()


def create_schema(conn):
    """
    :param conn: database connection

    Creates a new schema using the fully qualified name in Snowflake
    """
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE SCHEMA IF NOT EXISTS shop_db.sales_schema""")
        conn.commit()
        cursor.close()
        print("sales_schema created successfully.\n")

    except Exception as e:
        print(f"Error: {e}\n")
        conn.rollback()
        cursor.close()
