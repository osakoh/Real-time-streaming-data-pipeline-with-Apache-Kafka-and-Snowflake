from utils.sf_initial_setup import create_db_connection, create_db, create_schema

if __name__ == '__main__':
    create_db(create_db_connection())
    create_schema(create_db_connection())
