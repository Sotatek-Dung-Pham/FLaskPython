import psycopg2
from config import app_config

def get_db_connection(config_name):
    try:
        conn = psycopg2.connect(
            dbname = app_config[config_name].DB_NAME,
            host = app_config[config_name].HOST_NAME,
            user = app_config[config_name].USERNAME,
            password = app_config[config_name].PASSWORD
        )
        return conn

    except:
        print("I am unable to connect to the database")
