"""Python Functions workbook. Each small function is an answer example."""


# Levels 1-2: Basic functions and parameters

def greet():
    print("Hello, Welcome to Python!")


def welcome(name):
    print("Welcome,", name)


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        return "Cannot divide by zero"
    return first / second


def square(number):
    return number ** 2


def cube(number):
    return number ** 3


def is_even(number):
    return number % 2 == 0


def number_kind(number):
    if number > 0:
        return "positive"
    if number < 0:
        return "negative"
    return "zero"


def show_student(name, marks):
    print(name, "scored", marks)


def largest_of_three(first, second, third):
    largest = first
    if second > largest:
        largest = second
    if third > largest:
        largest = third
    return largest


def smallest_of_three(first, second, third):
    smallest = first
    if second < smallest:
        smallest = second
    if third < smallest:
        smallest = third
    return smallest


def factorial(number):
    answer = 1
    for value in range(1, number + 1):
        answer *= value
    return answer


def is_prime(number):
    if number < 2:
        return False
    for value in range(2, number):
        if number % value == 0:
            return False
    return True


def is_palindrome(text):
    return text == text[::-1]


def character_count(text):
    return len(text)


def vowel_count(text):
    return sum(letter.lower() in "aeiou" for letter in text)


def total_without_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def largest_without_max(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


# Level 3: Return values

def four_calculations(first, second):
    division = None if second == 0 else first / second
    return first + second, first - second, first * second, division


def grade(marks):
    if marks >= 90:
        return "A"
    if marks >= 80:
        return "B"
    if marks >= 70:
        return "C"
    if marks >= 50:
        return "D"
    return "F"


def average(numbers):
    if not numbers:
        return 0
    return total_without_sum(numbers) / len(numbers)


def only_even(numbers):
    return [number for number in numbers if is_even(number)]


def only_odd(numbers):
    return [number for number in numbers if not is_even(number)]


def reverse_text(text):
    return text[::-1]


def unique_values(values):
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result


def second_largest(numbers):
    values = sorted(set(numbers))
    if len(values) < 2:
        return None
    return values[-2]


def largest_and_smallest(numbers):
    return max(numbers), min(numbers)


# Level 4: Types of arguments

def price_with_tax(price, tax_percent=10):
    return price + price * tax_percent / 100


def show_student_info(name, age, course):
    print("Name:", name, "Age:", age, "Course:", course)


def rectangle_area(length, width):
    return length * width


def add_many(*numbers):
    return sum(numbers)


def largest_of_many(*numbers):
    if not numbers:
        return None
    return max(numbers)


def show_employee(**details):
    for key, value in details.items():
        print(key, "=", value)


def show_marks(name, *marks, **details):
    print("Name:", name)
    print("Marks:", marks)
    print("Details:", details)


def average_many(*numbers):
    return average(numbers)


def make_profile(**details):
    return details


def separate_even_odd(*numbers):
    return only_even(numbers), only_odd(numbers)


# Level 5: Nested, returned, recursive, and lambda functions

def outer_function():
    def inner_function():
        return "This is the inner function"
    return inner_function()


def make_greeter():
    def greet_name(name):
        return "Hello, " + name
    return greet_name


def recursive_factorial(number):
    if number <= 1:
        return 1
    return number * recursive_factorial(number - 1)


def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def sum_to(number):
    if number <= 0:
        return 0
    return number + sum_to(number - 1)


def recursive_reverse(text):
    if text == "":
        return text
    return recursive_reverse(text[1:]) + text[0]


square_lambda = lambda number: number ** 2
even_odd_lambda = lambda number: "even" if number % 2 == 0 else "odd"
largest_lambda = lambda first, second: first if first > second else second
rectangle_lambda = lambda length, width: length * width


# Lists, tuples, sets, and dictionaries

def min_max_tuple(numbers):
    return min(numbers), max(numbers)


def tuple_total(values):
    return total_without_sum(values)


def unique_count(values):
    return len(set(values))


def topper_name(marks_by_name):
    return max(marks_by_name, key=marks_by_name.get)


def keys_over_50(scores):
    return [name for name, score in scores.items() if score > 50]


def sorted_names(names):
    return sorted(names)


def even_odd_counts(numbers):
    counts = {"even": 0, "odd": 0}
    for number in numbers:
        key = "even" if is_even(number) else "odd"
        counts[key] += 1
    return counts


def character_frequency(text):
    counts = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    return counts


def word_frequency(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def squares_dictionary(numbers):
    return {number: number ** 2 for number in numbers}


# Mini-project building blocks: small functions that can be joined into menus.

def calculator(choice, first, second):
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "%": lambda a, b: a % b}
    if choice not in operations:
        return "Unknown operation"
    return operations[choice](first, second)


def add_student(records, name, marks):
    records[name] = marks


def search_student(records, name):
    return records.get(name)


def update_student(records, name, marks):
    if name in records:
        records[name] = marks


def delete_student(records, name):
    records.pop(name, None)


def bank_deposit(balance, amount):
    return balance + amount


def bank_withdraw(balance, amount):
    if amount > balance:
        return balance
    return balance - amount


def cart_total(cart):
    return sum(price * quantity for price, quantity in cart)


def add_contact(contacts, name, phone):
    contacts[name] = phone


def number_tools(number):
    return {"even": is_even(number), "prime": is_prime(number), "square": square(number)}


def library_search(books, title):
    return title in books


def main():
    greet()
    print("Add:", add(3, 4))
    print("Factorial:", factorial(5))
    print("Prime:", is_prime(7))
    print("Even numbers:", only_even([1, 2, 3, 4]))
    print("Grade:", grade(85))
    print("Student topper:", topper_name({"Ava": 88, "Ben": 72}))
    print("Calculator:", calculator("*", 6, 7))


if __name__ == "__main__":
    main()
