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


# 1. Create bank account table
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bank_accounts (
            account_id INT PRIMARY KEY,
            holder_name VARCHAR(100),
            balance INT
        )
    """)
    cursor.execute("INSERT INTO bank_accounts (account_id, holder_name, balance) VALUES (1, 'Alice', 1000)")
    cursor.execute("INSERT INTO bank_accounts (account_id, holder_name, balance) VALUES (2, 'Bob', 500)")
    connection.commit()
    connection.close()


# 2. Deposit and withdraw
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("UPDATE bank_accounts SET balance = balance + 200 WHERE account_id = 1")
    cursor.execute("UPDATE bank_accounts SET balance = balance - 100 WHERE account_id = 2")
    connection.commit()
    print("Deposit and withdrawal completed.")
    connection.close()


# 3. Demonstrate commit and rollback
connection = connect_db()
if connection:
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE bank_accounts SET balance = balance + 100 WHERE account_id = 1")
        connection.commit()
        print("Commit successful.")

        cursor.execute("UPDATE bank_accounts SET balance = balance - 1000 WHERE account_id = 2")
        connection.rollback()
        print("Rollback executed.")
    except Error as e:
        print(f"Transaction error: {e}")
        connection.rollback()
    finally:
        connection.close()


# 4. Order system and stock update
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INT PRIMARY KEY, product_name VARCHAR(100), stock INT)")
    cursor.execute("INSERT INTO products (product_id, product_name, stock) VALUES (1, 'Notebook', 20)")
    cursor.execute("INSERT INTO products (product_id, product_name, stock) VALUES (2, 'Pen', 50)")
    connection.commit()
    connection.close()


connection = connect_db()
if connection:
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE products SET stock = stock - 1 WHERE product_id = 1")
        connection.commit()
        print("Product stock updated.")
    except Error as e:
        connection.rollback()
        print(f"Stock update error: {e}")
    finally:
        connection.close()


# 5. Rollback when error occurs
connection = connect_db()
if connection:
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE bank_accounts SET balance = balance + 500 WHERE account_id = 1")
        raise Exception("Sample error to demonstrate rollback.")
    except Exception as e:
        connection.rollback()
        print(f"Rollback due to error: {e}")
    finally:
        connection.close()


# 6. Backup table example
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS student_backup AS SELECT * FROM students")
    connection.commit()
    print("Backup table created.")
    connection.close()


# 7. Copy records from one table to another
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students_copy AS SELECT * FROM students")
    connection.commit()
    print("Records copied to students_copy.")
    connection.close()


# 8. Delete multiple records based on condition
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE marks < 70")
    connection.commit()
    print("Multiple records deleted.")
    connection.close()


# 9. Update multiple records based on condition
connection = connect_db()
if connection:
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET marks = marks + 5 WHERE course = 'Math'")
    connection.commit()
    print("Multiple records updated.")
    connection.close()


# 10. Parameterized SQL queries
connection = connect_db()
if connection:
    cursor = connection.cursor()
    student_id = 1
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    row = cursor.fetchone()
    print("Parameterized query result:", row)
    connection.close()
