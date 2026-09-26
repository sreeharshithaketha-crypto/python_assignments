import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="college_db"
        )

    def close(self):
        if self.connection.is_connected():
            self.connection.close()


class Student:
    def __init__(self):
        self.db = DatabaseConnection()

    def insert_student(self, student_id, name, age, course, marks):
        cursor = self.db.connection.cursor()
        cursor.execute(
            "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)",
            (student_id, name, age, course, marks)
        )
        self.db.connection.commit()
        print("Student inserted with class method.")

    def get_students(self):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def delete_student(self, student_id):
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        self.db.connection.commit()
        print("Student deleted with class method.")


class Employee:
    def __init__(self):
        self.db = DatabaseConnection()

    def insert_employee(self, employee_id, name, department, salary):
        cursor = self.db.connection.cursor()
        cursor.execute(
            "INSERT INTO employees (id, name, department, salary, joining_date) VALUES (%s, %s, %s, %s, CURDATE())",
            (employee_id, name, department, salary)
        )
        self.db.connection.commit()
        print("Employee inserted.")


class DatabaseManager:
    def __init__(self):
        self.db = DatabaseConnection()

    def commit(self):
        self.db.connection.commit()

    def rollback(self):
        self.db.connection.rollback()

    def close(self):
        self.db.close()


student = Student()
student.insert_student(9, "Ivy", 21, "English", 72)
student.get_students()
student.delete_student(9)

employee = Employee()
employee.insert_employee(11, "Jatin", "IT", 70000)

manager = DatabaseManager()
manager.commit()
manager.close()
