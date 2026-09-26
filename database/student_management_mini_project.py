import mysql.connector
from mysql.connector import Error


# Simple student management mini project

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


# Create table if not exists
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            course VARCHAR(100),
            marks INT
        )
    """)
    connection.commit()
    connection.close()


# CRUD functions

def add_student(student_id, name, age, course, marks):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)",
            (student_id, name, age, course, marks)
        )
        connection.commit()
        print("Student added.")
        connection.close()


def view_students():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.close()


def update_student(student_id, new_name, new_marks):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = %s, marks = %s WHERE id = %s", (new_name, new_marks, student_id))
        connection.commit()
        print("Student updated.")
        connection.close()


def delete_student(student_id):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        connection.commit()
        print("Student deleted.")
        connection.close()


# Example usage
add_student(10, "John", 22, "Computer Science", 92)
view_students()
update_student(10, "John Smith", 95)
delete_student(10)
