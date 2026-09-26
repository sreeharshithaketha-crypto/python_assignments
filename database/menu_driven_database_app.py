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


def add_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
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
        print("Student inserted.")
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


def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    marks = int(input("Enter new marks: "))

    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = %s, marks = %s WHERE id = %s", (name, marks, student_id))
        connection.commit()
        print("Student updated.")
        connection.close()


def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        connection.commit()
        print("Student deleted.")
        connection.close()


while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
