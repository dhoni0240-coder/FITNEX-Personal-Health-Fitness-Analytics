import mysql.connector
from mysql.connector import Error

from config.settings import DB_CONFIG


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            return connection

    except Error as error:
        print(f"MySQL Connection Error: {error}")

    return None


def test_connection():
    connection = get_connection()

    if connection:
        try:
            print("FITNEX Database Connected Successfully!")
            print(f"Database: {DB_CONFIG['database']}")
            return True

        finally:
            connection.close()

    print("Database Connection Failed!")
    return False