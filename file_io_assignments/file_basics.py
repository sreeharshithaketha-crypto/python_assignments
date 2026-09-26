"""File I/O workbook: Levels 1-3 (basic operations, modes, and methods).

Run this file to try the examples. It creates sample.txt beside this script.
"""

from pathlib import Path


FOLDER = Path(__file__).parent
SAMPLE_FILE = FOLDER / "sample.txt"


# Level 1: Basic file operations

def create_welcome_file():
    with open(SAMPLE_FILE, "w", encoding="utf-8") as file:
        file.write("Welcome to Python\n")


def write_person(name, age, course):
    with open(FOLDER / "person.txt", "w", encoding="utf-8") as file:
        file.write(f"Name: {name}\nAge: {age}\nCourse: {course}\n")


def write_student_names(names):
    with open(FOLDER / "students.txt", "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")


def write_numbers(numbers):
    with open(FOLDER / "numbers.txt", "w", encoding="utf-8") as file:
        for number in numbers:
            file.write(str(number) + "\n")


def read_complete(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def read_characters(path):
    with open(path, "r", encoding="utf-8") as file:
        for character in file.read():
            print(character)


def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")


def read_lines_as_list(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def show_first_five(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file.readlines()[:5]:
            print(line, end="")


def show_last_five(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file.readlines()[-5:]:
            print(line, end="")


# Level 2: File modes

def write_multiple_lines(path, lines):
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(line + "\n" for line in lines)


def append_text(path, text):
    with open(path, "a", encoding="utf-8") as file:
        file.write(text + "\n")


def file_exists(path):
    return Path(path).exists()


def create_if_missing(path):
    with open(path, "x", encoding="utf-8") as file:
        file.write("This file was new.\n")


def overwrite_file(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)


def append_student(path, name, age, course):
    append_text(path, f"{name}, {age}, {course}")


def clear_file(path):
    open(path, "w", encoding="utf-8").close()


def create_read_append(path):
    with open(path, "w", encoding="utf-8") as file:
        file.write("First line\n")
    print(read_complete(path), end="")
    append_text(path, "Added line")
    print(read_complete(path), end="")


# Level 3: File methods

def read_first_characters(path, count):
    with open(path, "r", encoding="utf-8") as file:
        return file.read(count)


def read_one_line(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readline()


def read_all_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def write_one_line(path, line):
    with open(path, "w", encoding="utf-8") as file:
        file.write(line + "\n")


def write_many_lines(path, lines):
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(line + "\n" for line in lines)


def show_pointer_positions(path):
    with open(path, "r", encoding="utf-8") as file:
        print("Start:", file.tell())
        print("Text:", file.read(5))
        print("After reading 5 characters:", file.tell())
        file.seek(0)
        print("After seek(0):", file.tell())


def main():
    FOLDER.mkdir(exist_ok=True)
    write_multiple_lines(SAMPLE_FILE, ["Welcome to Python", "File I/O is easy", "Practice every day"])
    write_person("Alex", 10, "Python")
    write_student_names(["Ava", "Ben", "Kai", "Mia", "Zoe"])
    write_numbers([1, 2, 3, 4, 5])

    print("Complete file:")
    print(read_complete(SAMPLE_FILE), end="")
    print("First 5 characters:", read_first_characters(SAMPLE_FILE, 5))
    print("First line:", read_one_line(SAMPLE_FILE), end="")
    print("All lines:", read_all_lines(SAMPLE_FILE))
    show_pointer_positions(SAMPLE_FILE)

    append_text(SAMPLE_FILE, "Appended with mode a")
    print("File exists:", file_exists(SAMPLE_FILE))
    print("First five lines:")
    show_first_five(SAMPLE_FILE)
    print("Last five lines:")
    show_last_five(SAMPLE_FILE)


if __name__ == "__main__":
    main()
