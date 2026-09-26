import mysql.connector
from mysql.connector import Error


def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="college_db"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Connection error: {e}")
        return None


def create_customer_table():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT PRIMARY KEY,
                customer_name VARCHAR(100),
                city VARCHAR(100)
            )
        """)
        connection.commit()
        connection.close()


create_customer_table()

connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO customers (customer_id, customer_name, city) VALUES (%s, %s, %s)",
        (1, "Sonia", "Delhi")
    )
    connection.commit()
    connection.close()

connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()
