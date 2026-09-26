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


def create_order_table():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders_management (
                order_id INT PRIMARY KEY,
                customer_id INT,
                amount INT
            )
        """)
        connection.commit()
        connection.close()


create_order_table()

connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO orders_management (order_id, customer_id, amount) VALUES (%s, %s, %s)",
        (1, 1, 1500)
    )
    connection.commit()
    connection.close()

connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders_management")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()
