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


# 1. Total number of records in students table
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    print("Total records in students:", cursor.fetchone()[0])
    connection.close()


# 2. Average marks of students
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(marks) FROM students")
    print("Average marks:", cursor.fetchone()[0])
    connection.close()


# 3. Highest marks
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(marks) FROM students")
    print("Highest marks:", cursor.fetchone()[0])
    connection.close()


# 4. Lowest marks
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT MIN(marks) FROM students")
    print("Lowest marks:", cursor.fetchone()[0])
    connection.close()


# Create orders table and sample data for remaining examples
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (order_id INT PRIMARY KEY, customer_name VARCHAR(100), total_amount INT)")
    cursor.execute("INSERT INTO orders (order_id, customer_name, total_amount) VALUES (1, 'Asha', 500)")
    cursor.execute("INSERT INTO orders (order_id, customer_name, total_amount) VALUES (2, 'Rohan', 700)")
    cursor.execute("INSERT INTO orders (order_id, customer_name, total_amount) VALUES (3, 'Asha', 300)")
    connection.commit()
    connection.close()


# 5. Total sales from orders table
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(total_amount) FROM orders")
    print("Total sales:", cursor.fetchone()[0])
    connection.close()


# 6. Total sales per customer
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT customer_name, SUM(total_amount) FROM orders GROUP BY customer_name")
    rows = cursor.fetchall()
    print("Total sales per customer:")
    for row in rows:
        print(row)
    connection.close()


# 7. Average salary per department
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT department, AVG(salary) FROM employees GROUP BY department")
    rows = cursor.fetchall()
    print("\nAverage salary per department:")
    for row in rows:
        print(row)
    connection.close()


# 8. Count students in each course
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT course, COUNT(*) FROM students GROUP BY course")
    rows = cursor.fetchall()
    print("\nStudents in each course:")
    for row in rows:
        print(row)
    connection.close()
