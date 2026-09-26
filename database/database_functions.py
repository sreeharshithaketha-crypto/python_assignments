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


# 1. add_student()
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


# 2. get_students()
def get_students():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.close()


# 3. search_student()
def search_student(value):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE id = %s OR name = %s", (value, value))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.close()


# 4. update_student()
def update_student(student_id, new_name, new_marks):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = %s, marks = %s WHERE id = %s", (new_name, new_marks, student_id))
        connection.commit()
        print("Student updated.")
        connection.close()


# 5. delete_student()
def delete_student(student_id):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        connection.commit()
        print("Student deleted.")
        connection.close()


# Example function calls
add_student(8, "Heena", 20, "Biology", 81)
get_students()
search_student(8)
update_student(8, "Heena Sharma", 85)
delete_student(8)
