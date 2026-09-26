"""File I/O workbook: Levels 4-6 (processing, changes, and number files)."""

from pathlib import Path


FOLDER = Path(__file__).parent


def read_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def count_text(path):
    text = read_text(path)
    lines = text.splitlines()
    words = text.split()
    vowels = "aeiouAEIOU"
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", len(text))
    print("Vowels:", sum(character in vowels for character in text))
    print("Consonants:", sum(character.isalpha() and character not in vowels for character in text))
    print("Digits:", sum(character.isdigit() for character in text))
    print("Spaces:", text.count(" "))
    print("Uppercase:", sum(character.isupper() for character in text))
    print("Lowercase:", sum(character.islower() for character in text))


def show_matching_lines(path, word):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if word in line:
                print(line, end="")


def show_lines_starting_with(path, first_character):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(first_character):
                print(line, end="")


def save_even_numbers(source, destination):
    numbers = read_numbers(source)
    write_numbers(destination, [number for number in numbers if number % 2 == 0])


def save_odd_numbers(source, destination):
    numbers = read_numbers(source)
    write_numbers(destination, [number for number in numbers if number % 2 != 0])


def replace_word(source, destination, old_word, new_word):
    text = read_text(source).replace(old_word, new_word)
    write_text(destination, text)


def remove_blank_lines(source, destination):
    lines = read_text(source).splitlines()
    write_text(destination, "".join(line + "\n" for line in lines if line.strip()))


def remove_extra_spaces(source, destination):
    lines = read_text(source).splitlines()
    write_text(destination, "".join(" ".join(line.split()) + "\n" for line in lines))


def change_case(source, destination, to_upper=True):
    text = read_text(source)
    write_text(destination, text.upper() if to_upper else text.lower())


def reverse_each_line(source, destination):
    lines = read_text(source).splitlines()
    write_text(destination, "".join(line[::-1] + "\n" for line in lines))


def reverse_file(source, destination):
    write_text(destination, read_text(source)[::-1])


def remove_duplicate_lines(source, destination):
    lines = read_text(source).splitlines()
    unique_lines = []
    for line in lines:
        if line not in unique_lines:
            unique_lines.append(line)
    write_text(destination, "".join(line + "\n" for line in unique_lines))


def read_numbers(path):
    with open(path, "r", encoding="utf-8") as file:
        return [int(line.strip()) for line in file if line.strip()]


def write_numbers(path, numbers):
    with open(path, "w", encoding="utf-8") as file:
        for number in numbers:
            file.write(str(number) + "\n")


def number_report(path):
    numbers = read_numbers(path)
    if not numbers:
        print("There are no numbers.")
        return
    print("Total:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))
    print("Positive:", sum(number > 0 for number in numbers))
    print("Negative:", sum(number < 0 for number in numbers))
    print("Zero:", sum(number == 0 for number in numbers))
    duplicates = []
    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
    print("Duplicates:", duplicates)


def save_separated_numbers(source, even_file, odd_file):
    numbers = read_numbers(source)
    write_numbers(even_file, [number for number in numbers if number % 2 == 0])
    write_numbers(odd_file, [number for number in numbers if number % 2 != 0])


def save_powers(source, square_file, cube_file):
    numbers = read_numbers(source)
    write_numbers(square_file, [number ** 2 for number in numbers])
    write_numbers(cube_file, [number ** 3 for number in numbers])


def save_sorted_numbers(source, destination):
    write_numbers(destination, sorted(read_numbers(source)))


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    FOLDER.mkdir(exist_ok=True)
    text_file = FOLDER / "processing_sample.txt"
    numbers_file = FOLDER / "processing_numbers.txt"
    write_text(text_file, "Python is Fun 123\nhello world\n\nPython is Fun 123\n")
    write_numbers(numbers_file, [5, 2, -3, 0, 2, 8, 1])

    count_text(text_file)
    print("Lines containing Python:")
    show_matching_lines(text_file, "Python")
    print("Lines starting with h:")
    show_lines_starting_with(text_file, "h")
    number_report(numbers_file)

    save_even_numbers(numbers_file, FOLDER / "even_numbers.txt")
    save_odd_numbers(numbers_file, FOLDER / "odd_numbers.txt")
    save_powers(numbers_file, FOLDER / "squares.txt", FOLDER / "cubes.txt")
    save_sorted_numbers(numbers_file, FOLDER / "sorted_numbers.txt")
    change_case(text_file, FOLDER / "uppercase.txt")
    remove_duplicate_lines(text_file, FOLDER / "unique_lines.txt")
    print("Example output files were saved in:", FOLDER)


if __name__ == "__main__":
    main()
