import oracledb
import os
import logging
from dotenv import load_dotenv
from payload import payload_type

load_dotenv()

oracledb.init_oracle_client()


# Database connection
db_conn_string = os.environ["db_conn_string"]
db_user = os.environ["db_user"]
db_password = os.environ["db_password"]


def database_conn():
    try:
        conn = oracledb.connect(user=db_user, password=db_password, dsn=db_conn_string)
        cur = conn.cursor()
        print(f"Successfully connected to Oracle")
    except oracledb.Error as e:
        print(f"database error: {e}")

    return conn, cur


def main():
    database_conn()

if __name__ == "__main__":
    main()