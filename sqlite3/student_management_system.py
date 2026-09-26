import sqlite3


# Part C 30: a small class to hold our database functions.
class Database:
    def __init__(self):
        # Part A 1: connect to college.db.
        self.db = sqlite3.connect("college.db")
        self.db.execute("PRAGMA foreign_keys = ON")
        self.create_tables()

    def create_tables(self):
        # Part A 2 and Part C 25-26: create tables and relationships.
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT, age INTEGER, course TEXT, marks REAL
            );
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            );
            CREATE TABLE IF NOT EXISTS enrollments (
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            );
        """)
        # Part C 33: indexes can make searching faster.
        self.db.execute("CREATE INDEX IF NOT EXISTS marks_index ON students(marks)")
        self.db.execute("CREATE INDEX IF NOT EXISTS name_index ON students(name)")
        self.db.commit()

    # Part A 3 and Part C 34: add one student in a transaction.
    def add_student(self, name, age, course, marks):
        try:
            student = self.db.execute(
                "INSERT INTO students(name, age, course, marks) VALUES (?, ?, ?, ?)",
                (name, age, course, marks),
            )
            self.db.execute("INSERT OR IGNORE INTO courses(name) VALUES (?)", (course,))
            course_id = self.db.execute(
                "SELECT id FROM courses WHERE name=?", (course,)
            ).fetchone()[0]
            self.db.execute(
                "INSERT INTO enrollments VALUES (?, ?)", (student.lastrowid, course_id)
            )
            self.db.commit()
        except sqlite3.Error:
            self.db.rollback()
            raise

    # Part B 11: add many students with executemany().
    def add_many(self, students):
        try:
            self.db.executemany(
                "INSERT INTO students(name, age, course, marks) VALUES (?, ?, ?, ?)",
                students,
            )
            for student in students:
                self.db.execute("INSERT OR IGNORE INTO courses(name) VALUES (?)", (student[2],))
                student_id = self.db.execute(
                    "SELECT id FROM students WHERE name=? ORDER BY id DESC LIMIT 1",
                    (student[0],),
                ).fetchone()[0]
                course_id = self.db.execute(
                    "SELECT id FROM courses WHERE name=?", (student[2],)
                ).fetchone()[0]
                self.db.execute(
                    "INSERT INTO enrollments VALUES (?, ?)", (student_id, course_id)
                )
            self.db.commit()
        except sqlite3.Error:
            self.db.rollback()
            raise

    # Part A 4 and Part C 32: show students, using LIMIT/OFFSET for pages.
    def show_students(self, limit=None, offset=0):
        sql = "SELECT * FROM students ORDER BY id"
        values = ()
        if limit:
            sql += " LIMIT ? OFFSET ?"
            values = (limit, offset)
        return self.db.execute(sql, values).fetchall()

    # Part A 5-8 and Part C 31: search by name, course, and marks.
    def search(self, name="", course="", low=0, high=100):
        return self.db.execute("""
            SELECT * FROM students
            WHERE name LIKE ? AND course LIKE ? AND marks BETWEEN ? AND ?
        """, (name + "%", "%" + course + "%", low, high)).fetchall()

    # Part A 9: update marks or other student details.
    def update_student(self, student_id, name, age, course, marks):
        try:
            self.db.execute("""
                UPDATE students SET name=?, age=?, course=?, marks=? WHERE id=?
            """, (name, age, course, marks, student_id))
            self.db.execute("INSERT OR IGNORE INTO courses(name) VALUES (?)", (course,))
            course_id = self.db.execute(
                "SELECT id FROM courses WHERE name=?", (course,)
            ).fetchone()[0]
            self.db.execute("DELETE FROM enrollments WHERE student_id=?", (student_id,))
            self.db.execute(
                "INSERT INTO enrollments VALUES (?, ?)", (student_id, course_id)
            )
            self.db.commit()
        except sqlite3.Error:
            self.db.rollback()
            raise

    # Part A 10: delete a student.
    def delete_student(self, student_id):
        self.db.execute("DELETE FROM enrollments WHERE student_id=?", (student_id,))
        self.db.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.db.commit()

    # Part B 12-13: order marks and show the top 3.
    def top_students(self):
        return self.db.execute(
            "SELECT * FROM students ORDER BY marks DESC LIMIT 3"
        ).fetchall()

    # Part B 14-16: COUNT, AVG, MAX, and MIN.
    def statistics(self):
        return self.db.execute(
            "SELECT COUNT(*), AVG(marks), MAX(marks), MIN(marks) FROM students"
        ).fetchone()

    # Part B 17-18: GROUP BY course.
    def course_statistics(self):
        return self.db.execute("""
            SELECT course, COUNT(*), AVG(marks)
            FROM students GROUP BY course
        """).fetchall()

    # Part C 27: show student names with course names using JOIN.
    def joined_students(self):
        return self.db.execute("""
            SELECT students.name, courses.name
            FROM students JOIN enrollments
            ON students.id = enrollments.student_id
            JOIN courses ON courses.id = enrollments.course_id
        """).fetchall()

    # Part C 28: find students with no enrollment.
    def students_without_courses(self):
        return self.db.execute("""
            SELECT students.name FROM students LEFT JOIN enrollments
            ON students.id = enrollments.student_id
            WHERE enrollments.student_id IS NULL
        """).fetchall()

    def close(self):
        self.db.close()


def show(rows):
    for row in rows:
        print(row)
    if not rows:
        print("No records found.")


def details():
    # Read one student's details from the user.
    return (
        input("Name: "), int(input("Age: ")),
        input("Course: "), float(input("Marks: ")),
    )


def menu(database):
    # Part B 21 and Final Challenge: menu-driven application.
    while True:
        print("\n1 Add  2 View  3 Search  4 Update  5 Delete")
        print("6 Top 3  7 Course Stats  8 Statistics  9 Page  0 Exit")
        choice = input("Choose: ")

        try:
            if choice == "1":
                database.add_student(*details())
                print("Student added.")
            elif choice == "2":
                show(database.show_students())
            elif choice == "3":
                name = input("Name starts with: ")
                course = input("Course: ")
                low = float(input("Lowest marks: "))
                high = float(input("Highest marks: "))
                show(database.search(name, course, low, high))
            elif choice == "4":
                student_id = int(input("Student ID: "))
                database.update_student(student_id, *details())
                print("Student updated.")
            elif choice == "5":
                student_id = int(input("Student ID: "))
                database.delete_student(student_id)
                print("Student deleted.")
            elif choice == "6":
                show(database.top_students())
            elif choice == "7":
                show(database.course_statistics())
            elif choice == "8":
                print("Count, Average, Highest, Lowest:", database.statistics())
            elif choice == "9":
                size = int(input("Students per page: "))
                page = int(input("Page number: "))
                show(database.show_students(size, (page - 1) * size))
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, sqlite3.Error) as error:
            print("Error:", error)


if __name__ == "__main__":
    database = Database()
    try:
        # Part A 3 and Part B 11: insert 10 example records once.
        if database.db.execute("SELECT COUNT(*) FROM students").fetchone()[0] == 0:
            database.add_many([
                ("Asha", 20, "Python", 88), ("Ravi", 21, "SQL", 76),
                ("Maya", 19, "Python", 94), ("John", 22, "Java", 68),
                ("Anita", 20, "Python", 82), ("Omar", 23, "SQL", 73),
                ("Priya", 21, "Java", 91), ("David", 20, "Python", 59),
                ("Sara", 22, "SQL", 87), ("Ali", 19, "Java", 64),
            ])
        menu(database)
    finally:
        database.close()
