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


# Create employees table
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100),
            salary INT,
            joining_date DATE
        )
    """)
    connection.commit()
    connection.close()


# Insert 10 employee records
records = [
    (1, "Riya", "IT", 60000, "2021-01-10"),
    (2, "Aman", "HR", 45000, "2020-05-15"),
    (3, "Karan", "IT", 75000, "2019-09-12"),
    (4, "Neha", "Finance", 55000, "2022-02-20"),
    (5, "Rahul", "Marketing", 50000, "2021-06-25"),
    (6, "Priya", "IT", 80000, "2018-11-01"),
    (7, "Zoya", "Finance", 65000, "2020-08-18"),
    (8, "Amit", "Sales", 47000, "2023-01-05"),
    (9, "Sara", "HR", 52000, "2017-12-27"),
    (10, "Vikram", "Sales", 68000, "2022-07-14")
]

connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.executemany(
        "INSERT INTO employees (id, name, department, salary, joining_date) VALUES (%s, %s, %s, %s, %s)",
        records
    )
    connection.commit()
    connection.close()


# 3. Display employees whose salary > 50000
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE salary > 50000")
    rows = cursor.fetchall()
    print("Employees with salary > 50000:")
    for row in rows:
        print(row)
    connection.close()


# 4. Display employees belonging to IT
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE department = 'IT'")
    rows = cursor.fetchall()
    print("\nEmployees in IT department:")
    for row in rows:
        print(row)
    connection.close()


# 5. Display sorted ascending by salary
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees ORDER BY salary ASC")
    rows = cursor.fetchall()
    print("\nEmployees sorted by salary ascending:")
    for row in rows:
        print(row)
    connection.close()


# 6. Display sorted descending by salary
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees ORDER BY salary DESC")
    rows = cursor.fetchall()
    print("\nEmployees sorted by salary descending:")
    for row in rows:
        print(row)
    connection.close()


# 7. Highest salary
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(salary) FROM employees")
    print("\nHighest salary:", cursor.fetchone()[0])
    connection.close()


# 8. Lowest salary
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT MIN(salary) FROM employees")
    print("Lowest salary:", cursor.fetchone()[0])
    connection.close()


# 9. Average salary
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(salary) FROM employees")
    print("Average salary:", cursor.fetchone()[0])
    connection.close()


# 10. Total salary paid
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(salary) FROM employees")
    print("Total salary paid:", cursor.fetchone()[0])
    connection.close()


# 11. Count employees in each department
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT department, COUNT(*) FROM employees GROUP BY department")
    rows = cursor.fetchall()
    print("\nEmployees by department:")
    for row in rows:
        print(row)
    connection.close()


# 12. Highest salary in each department
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT department, MAX(salary) FROM employees GROUP BY department")
    rows = cursor.fetchall()
    print("\nHighest salary in each department:")
    for row in rows:
        print(row)
    connection.close()


# 13. Employees joined after a particular date
join_date = "2020-01-01"
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE joining_date > %s", (join_date,))
    rows = cursor.fetchall()
    print(f"\nEmployees joined after {join_date}:")
    for row in rows:
        print(row)
    connection.close()


# 14. Names beginning with a particular letter
letter = "A"
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE name LIKE %s", (letter + '%',))
    rows = cursor.fetchall()
    print(f"\nEmployees whose names start with {letter}:")
    for row in rows:
        print(row)
    connection.close()


# 15. Salary within range
min_salary = 45000
max_salary = 70000
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE salary BETWEEN %s AND %s", (min_salary, max_salary))
    rows = cursor.fetchall()
    print(f"\nEmployees with salary between {min_salary} and {max_salary}:")
    for row in rows:
        print(row)
    connection.close()
