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


# 1. Create students and courses tables with relationship
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS courses (course_id INT PRIMARY KEY, course_name VARCHAR(100))")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students_with_courses (
            student_id INT PRIMARY KEY,
            name VARCHAR(100),
            course_id INT,
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    """)
    connection.commit()
    connection.close()


# Insert sample data
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO courses (course_id, course_name) VALUES (1, 'Computer Science')")
    cursor.execute("INSERT INTO courses (course_id, course_name) VALUES (2, 'Math')")
    cursor.execute("INSERT INTO students_with_courses (student_id, name, course_id) VALUES (1, 'Alice', 1)")
    cursor.execute("INSERT INTO students_with_courses (student_id, name, course_id) VALUES (2, 'Bob', 2)")
    connection.commit()
    connection.close()


# 5. Retrieve students with course names using JOIN
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT s.student_id, s.name, c.course_name
        FROM students_with_courses s
        JOIN courses c ON s.course_id = c.course_id
    """)
    rows = cursor.fetchall()
    print("Students with course names:")
    for row in rows:
        print(row)
    connection.close()


# Additional sample tables for customers and orders
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS customers (customer_id INT PRIMARY KEY, customer_name VARCHAR(100))")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY,
            customer_id INT,
            amount INT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)
    connection.commit()
    connection.close()


# Sample customer orders
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customers (customer_id, customer_name) VALUES (1, 'Asha')")
    cursor.execute("INSERT INTO customers (customer_id, customer_name) VALUES (2, 'Rohan')")
    cursor.execute("INSERT INTO orders (order_id, customer_id, amount) VALUES (1, 1, 300)")
    cursor.execute("INSERT INTO orders (order_id, customer_id, amount) VALUES (2, 1, 200)")
    cursor.execute("INSERT INTO orders (order_id, customer_id, amount) VALUES (3, 2, 500)")
    connection.commit()
    connection.close()


# 6. Retrieve customers with orders
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.customer_id, c.customer_name, o.order_id, o.amount
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
    """)
    rows = cursor.fetchall()
    print("\nCustomers with orders:")
    for row in rows:
        print(row)
    connection.close()


# 8. Find departments with no employees
# This example uses the existing employees table from earlier level
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS departments (department_id INT PRIMARY KEY, department_name VARCHAR(100))")
    cursor.execute("INSERT INTO departments (department_id, department_name) VALUES (1, 'IT')")
    cursor.execute("INSERT INTO departments (department_id, department_name) VALUES (2, 'HR')")
    cursor.execute("INSERT INTO departments (department_id, department_name) VALUES (3, 'Finance')")
    connection.commit()
    connection.close()


connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT d.department_name
        FROM departments d
        LEFT JOIN employees e ON d.department_name = e.department
        WHERE e.id IS NULL
    """)
    rows = cursor.fetchall()
    print("\nDepartments with no employees:")
    for row in rows:
        print(row)
    connection.close()
