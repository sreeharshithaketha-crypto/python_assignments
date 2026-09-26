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


# 1. Accept student details from user and insert
student_id = int(input("Enter student ID: "))
name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course: ")
marks = int(input("Enter marks: "))

connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)",
        (student_id, name, age, course, marks)
    )
    connection.commit()
    print("Student inserted successfully.")
    connection.close()


# 2. Accept student ID and display details
student_id = int(input("\nEnter student ID to search: "))
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    row = cursor.fetchone()
    if row:
        print("Student details:", row)
    else:
        print("Student not found.")
    connection.close()


# 3. Accept student ID and new marks and update
student_id = int(input("\nEnter student ID to update marks: "))
new_marks = int(input("Enter new marks: "))
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET marks = %s WHERE id = %s", (new_marks, student_id))
    connection.commit()
    print("Marks updated.")
    connection.close()


# 4. Accept student ID and delete record
student_id = int(input("\nEnter student ID to delete: "))
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    connection.commit()
    print("Student deleted.")
    connection.close()


# 5. Accept course name and display all students
course = input("\nEnter course name: ")
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE course = %s", (course,))
    rows = cursor.fetchall()
    print(f"Students in {course}:")
    for row in rows:
        print(row)
    connection.close()


# 6. Accept minimum and maximum marks
min_marks = int(input("\nEnter minimum marks: "))
max_marks = int(input("Enter maximum marks: "))
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE marks BETWEEN %s AND %s", (min_marks, max_marks))
    rows = cursor.fetchall()
    print(f"Students with marks between {min_marks} and {max_marks}:")
    for row in rows:
        print(row)
    connection.close()


# 7. Accept student name and search
name = input("\nEnter student name: ")
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
    rows = cursor.fetchall()
    print(f"Students named {name}:")
    for row in rows:
        print(row)
    connection.close()
