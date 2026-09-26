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


def create_product_table():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INT PRIMARY KEY,
                product_name VARCHAR(100),
                price INT,
                stock INT
            )
        """)
        connection.commit()
        connection.close()


create_product_table()

connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO products (product_id, product_name, price, stock) VALUES (%s, %s, %s, %s)",
        (1, "Laptop", 45000, 10)
    )
    connection.commit()
    connection.close()

connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()
