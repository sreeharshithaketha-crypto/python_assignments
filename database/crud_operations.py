import mysql.connector
from mysql.connector import Error


# 1. Insert a new student
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
            (7, "Grace", 24, "History", 95)
        )
        connection.commit()
        print("New student inserted.")

except Error as e:
    print(f"Insert error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 2. Update a student's name
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = 'Grace Hopper' WHERE id = 7")
        connection.commit()
        print("Student name updated.")

except Error as e:
    print(f"Update name error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 3. Update a student's marks
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET marks = 96 WHERE id = 7")
        connection.commit()
        print("Student marks updated.")

except Error as e:
    print(f"Update marks error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 4. Update a student's course
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET course = 'Computer Science' WHERE id = 7")
        connection.commit()
        print("Student course updated.")

except Error as e:
    print(f"Update course error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 5. Delete a student by ID
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = 7")
        connection.commit()
        print("Student deleted.")

except Error as e:
    print(f"Delete error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 6. Search student by ID
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE id = 3")
        row = cursor.fetchone()
        print("\nStudent with id 3:")
        print(row)

except Error as e:
    print(f"Search by ID error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 7. Search students by name
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE name LIKE '%Alice%'")
        rows = cursor.fetchall()
        print("\nStudents matching name Alice:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Search by name error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 8. Display students with marks between 50 and 80
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE marks BETWEEN 50 AND 80")
        rows = cursor.fetchall()
        print("\nStudents with marks between 50 and 80:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Range query error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 9. Display students in descending order of marks
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students ORDER BY marks DESC")
        rows = cursor.fetchall()
        print("\nStudents sorted by marks descending:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Descending sort error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()


# 10. Display top 5 students based on marks
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college_db"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 5")
        rows = cursor.fetchall()
        print("\nTop 5 students by marks:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Top 5 query error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
