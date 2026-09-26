"""File I/O workbook: student records, CSV, JSON, and safe file operations."""

import csv
import json
import shutil
import sys
from pathlib import Path


FOLDER = Path(__file__).parent
STUDENT_FIELDS = ["id", "name", "age", "course", "marks"]


def write_student_records(path, students):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
        writer.writeheader()
        writer.writerows(students)


def read_student_records(path):
    with open(path, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def find_student_by_name(path, name):
    for student in read_student_records(path):
        if student["name"].lower() == name.lower():
            return student
    return None


def find_student_by_id(path, student_id):
    for student in read_student_records(path):
        if student["id"] == str(student_id):
            return student
    return None


def update_student_marks(path, student_id, marks):
    students = read_student_records(path)
    for student in students:
        if student["id"] == str(student_id):
            student["marks"] = str(marks)
    write_student_records(path, students)


def delete_student(path, student_id):
    students = read_student_records(path)
    kept_students = [student for student in students if student["id"] != str(student_id)]
    write_student_records(path, kept_students)


def show_student_results(path):
    students = read_student_records(path)
    if not students:
        print("There are no student records.")
        return
    topper = max(students, key=lambda student: float(student["marks"]))
    average = sum(float(student["marks"]) for student in students) / len(students)
    print("Top student:", topper["name"], topper["marks"])
    print("Average marks:", average)
    print("Above 75:", [student["name"] for student in students if float(student["marks"]) > 75])


def write_student_csv(path, students):
    write_student_records(path, students)


def add_student_csv(path, student):
    file_exists = Path(path).exists()
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
        if not file_exists or Path(path).stat().st_size == 0:
            writer.writeheader()
        writer.writerow(student)


def search_student_csv(path, student_id):
    return find_student_by_id(path, student_id)


def update_student_csv_marks(path, student_id, marks):
    update_student_marks(path, student_id, marks)


def delete_student_csv(path, student_id):
    delete_student(path, student_id)


def csv_report(path):
    students = read_student_records(path)
    if not students:
        return
    topper = max(students, key=lambda student: float(student["marks"]))
    print("Topper:", topper["name"])
    print("Average:", sum(float(row["marks"]) for row in students) / len(students))
    print("Below 40:", [row["name"] for row in students if float(row["marks"]) < 40])


def sort_student_csv(source, destination):
    students = read_student_records(source)
    students.sort(key=lambda student: float(student["marks"]))
    write_student_records(destination, students)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def add_json_student(path, student):
    students = read_json(path)
    students.append(student)
    save_json(path, students)


def update_json_student(path, student_id, changes):
    students = read_json(path)
    for student in students:
        if student["id"] == student_id:
            student.update(changes)
    save_json(path, students)


def delete_json_student(path, student_id):
    students = read_json(path)
    students = [student for student in students if student["id"] != student_id]
    save_json(path, students)


def highest_salary_employee(path):
    employees = read_json(path)
    return max(employees, key=lambda employee: employee["salary"])


def inventory_value(path):
    products = read_json(path)
    return sum(product["price"] * product["quantity"] for product in products)


def safe_read(path):
    file = None
    try:
        file = open(path, "r", encoding="utf-8")
        return file.read()
    except FileNotFoundError:
        print("File was not found.")
        return ""
    except PermissionError:
        print("You do not have permission to read this file.")
        return ""
    finally:
        if file is not None:
            file.close()


def safe_read_numbers(path):
    numbers = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print("Skipping invalid number:", line.strip())
    except OSError as error:
        print("Could not read file:", error)
    return numbers


def safe_read_csv(path):
    try:
        return read_student_records(path)
    except (OSError, csv.Error) as error:
        print("Could not read CSV file:", error)
        return []


def safe_read_json(path):
    try:
        return read_json(path)
    except (OSError, json.JSONDecodeError) as error:
        print("Could not read JSON file:", error)
        return None


def copy_file(source, destination):
    try:
        shutil.copyfile(source, destination)
        print("File copied.")
    except OSError as error:
        print("Could not copy file:", error)


def file_manager():
    path = FOLDER / "managed_file.txt"
    while True:
        print("1 Create  2 Read  3 Write  4 Append  5 Search")
        print("6 Update  7 Copy  8 Rename  9 Delete  0 Exit")
        choice = input("Choose: ")
        try:
            if choice == "1":
                path.touch(exist_ok=True)
            elif choice == "2":
                print(safe_read(path))
            elif choice == "3":
                path.write_text(input("Text: "), encoding="utf-8")
            elif choice == "4":
                with open(path, "a", encoding="utf-8") as file:
                    file.write(input("Text: ") + "\n")
            elif choice == "5":
                print(input("Word: ") in safe_read(path))
            elif choice == "6":
                text = safe_read(path)
                old_text = input("Word to replace: ")
                new_text = input("New word: ")
                path.write_text(text.replace(old_text, new_text), encoding="utf-8")
            elif choice == "7":
                shutil.copyfile(path, FOLDER / "managed_copy.txt")
            elif choice == "8":
                new_path = FOLDER / "renamed_file.txt"
                path.rename(new_path)
                path = new_path
            elif choice == "9":
                path.unlink(missing_ok=True)
            elif choice == "0":
                break
            else:
                print("Choose a number from 0 to 9.")
        except (OSError, PermissionError) as error:
            print("File operation failed:", error)


def main():
    FOLDER.mkdir(exist_ok=True)
    students = [
        {"id": "1", "name": "Ava", "age": "18", "course": "Python", "marks": "88"},
        {"id": "2", "name": "Ben", "age": "19", "course": "Python", "marks": "72"},
        {"id": "3", "name": "Mia", "age": "18", "course": "Python", "marks": "39"},
    ]
    student_file = FOLDER / "students.csv"
    write_student_records(student_file, students)
    print("All students:", read_student_records(student_file))
    print("Find by name:", find_student_by_name(student_file, "Ava"))
    print("Find by ID:", find_student_by_id(student_file, "2"))
    csv_report(student_file)

    student_json = FOLDER / "students.json"
    save_json(student_json, [{"id": 1, "name": "Ava", "course": "Python"}])
    print("JSON students:", read_json(student_json))
    save_json(FOLDER / "employees.json", [{"name": "Sam", "salary": 50000}])
    save_json(FOLDER / "products.json", [{"name": "Pen", "price": 2, "quantity": 5}])
    print("Highest salary:", highest_salary_employee(FOLDER / "employees.json"))
    print("Inventory value:", inventory_value(FOLDER / "products.json"))
    print("Safe read missing file:", safe_read(FOLDER / "missing.txt"))


if __name__ == "__main__":
    if sys.argv[1:] == ["--menu"]:
        file_manager()
    else:
        main()
