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


# 1. Student Management Database
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students_management (id INT PRIMARY KEY, name VARCHAR(100), course VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS courses_management (course_id INT PRIMARY KEY, course_name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS enrollments (student_id INT, course_id INT)")
    connection.commit()
    connection.close()


# 2. Employee Management Database
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS departments_management (department_id INT PRIMARY KEY, department_name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS employees_management (employee_id INT PRIMARY KEY, name VARCHAR(100), department_id INT, salary INT)")
    connection.commit()
    connection.close()


# 3. E-Commerce Database
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS customers_ecommerce (customer_id INT PRIMARY KEY, customer_name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS products_ecommerce (product_id INT PRIMARY KEY, product_name VARCHAR(100), price INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders_ecommerce (order_id INT PRIMARY KEY, customer_id INT, total_amount INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS order_items (order_id INT, product_id INT, quantity INT)")
    connection.commit()
    connection.close()


# 4. Banking Database
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS customers_bank (customer_id INT PRIMARY KEY, customer_name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts (account_id INT PRIMARY KEY, customer_id INT, balance INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS transactions (transaction_id INT PRIMARY KEY, account_id INT, amount INT, type VARCHAR(50))")
    cursor.execute("CREATE TABLE IF NOT EXISTS branches (branch_id INT PRIMARY KEY, branch_name VARCHAR(100))")
    connection.commit()
    connection.close()


# 5. Hospital Database
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS patients (patient_id INT PRIMARY KEY, patient_name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS doctors (doctor_id INT PRIMARY KEY, doctor_name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS appointments (appointment_id INT PRIMARY KEY, patient_id INT, doctor_id INT, appointment_date DATE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS billing (bill_id INT PRIMARY KEY, patient_id INT, amount INT)")
    connection.commit()
    connection.close()


print("Advanced database project tables created successfully.")
