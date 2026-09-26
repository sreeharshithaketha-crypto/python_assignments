import mysql.connector
from mysql.connector import Error


def connect_db(database_name=None):
    """
    Simple MySQL connection helper for student assignments.
    Change the username and password below if your MySQL setup is different.
    """
    config = {
        "host": "localhost",
        "user": "root",
        "password": "",
    }

    if database_name:
        config["database"] = database_name

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connection successful!")
            return connection
    except Error as e:
        print(f"Connection error: {e}")
        return None

    return None


def close_connection(connection):
    if connection is not None and connection.is_connected():
        connection.close()
