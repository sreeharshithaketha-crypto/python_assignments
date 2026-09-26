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


def create_employee_table():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                department VARCHAR(100),
                salary INT
            )
        """)
        connection.commit()
        connection.close()


create_employee_table()


# Insert employee
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO employees (id, name, department, salary) VALUES (%s, %s, %s, %s)",
        (1, "Nisha", "IT", 60000)
    )
    connection.commit()
    connection.close()

# View employees
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()
