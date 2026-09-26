import mysql.connector
from mysql.connector import Error


# Step 1: create database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS college_db")
        print("Database college_db created or already exists.")

except Error as e:
    print(f"Database creation error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 2: create table
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
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
        print("Table students created or already exists.")

except Error as e:
    print(f"Table creation error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 3: connection message
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        print("Connection successful!")

except Error as e:
    print(f"Connection error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 4: insert one record
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)",
            (1, "Alice", 20, "Computer Science", 88)
        )
        connection.commit()
        print("One student record inserted.")

except Error as e:
    print(f"Insert error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 5: insert five records
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        records = [
            (2, "Bob", 21, "Math", 78),
            (3, "Charlie", 19, "Physics", 82),
            (4, "Diana", 22, "Computer Science", 90),
            (5, "Eve", 20, "Biology", 65),
            (6, "Frank", 23, "Math", 74)
        ]
        cursor.executemany(
            "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)",
            records
        )
        connection.commit()
        print("Five student records inserted.")

except Error as e:
    print(f"Insert all error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 6: retrieve all records
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        print("\nAll student records:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Select error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 7: retrieve names only
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM students")
        rows = cursor.fetchall()

        print("\nStudent names:")
        for row in rows:
            print(row[0])

except Error as e:
    print(f"Select names error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 8: retrieve marks greater than 75
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE marks > 75")
        rows = cursor.fetchall()

        print("\nStudents with marks greater than 75:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Query error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 9: retrieve by course
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE course = 'Computer Science'")
        rows = cursor.fetchall()

        print("\nStudents in Computer Science:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Course query error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# Step 10: count total number of students
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        count = cursor.fetchone()[0]
        print(f"\nTotal number of students: {count}")

except Error as e:
    print(f"Count error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
