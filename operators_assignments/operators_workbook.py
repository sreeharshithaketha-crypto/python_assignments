"""Python Operators workbook with small examples for all operator groups."""


# Level 1: Arithmetic operators

def arithmetic(first, second):
    division = None if second == 0 else first / second
    return {
        "addition": first + second,
        "subtraction": first - second,
        "multiplication": first * second,
        "division": division,
        "remainder": None if second == 0 else first % second,
        "floor division": None if second == 0 else first // second,
        "power": first ** second,
    }


def total_and_average(first, second, third):
    total = first + second + third
    return total, total / 3


def rectangle(length, width):
    return length * width, 2 * (length + width)


def simple_interest(principal, rate, years):
    return principal * rate * years / 100


# Level 2: Assignment operators

def assignment_steps(number):
    results = [number]
    number += 2
    results.append(number)
    number -= 1
    results.append(number)
    number *= 3
    results.append(number)
    number /= 2
    results.append(number)
    number //= 2
    results.append(number)
    number %= 3
    results.append(number)
    number **= 2
    results.append(number)
    return results


def shopping_bill(prices):
    total = 0
    for price in prices:
        total += price
    return total


# Level 3: Comparison operators

def compare(first, second):
    return {
        "equal": first == second,
        "not equal": first != second,
        "greater": first > second,
        "less": first < second,
        "greater or equal": first >= second,
        "less or equal": first <= second,
    }


def passed(marks):
    return marks > 50


def can_vote(age):
    return age >= 18


# Level 4: Logical operators

def between_10_and_50(number):
    return number >= 10 and number <= 50


def outside_10_to_100(number):
    return number < 10 or number > 100


def passed_both(math_marks, science_marks):
    return math_marks >= 35 and science_marks >= 35


def passed_one(math_marks, science_marks):
    return math_marks >= 35 or science_marks >= 35


def job_eligible(age, has_qualification):
    return age >= 18 and has_qualification


# Level 5: Membership operators

def is_present(item, collection):
    return item in collection


def is_missing(item, collection):
    return item not in collection


# Level 6: Identity operators

def identity_examples():
    first = [1, 2]
    same_list = first
    other_list = [1, 2]
    return {
        "same value": first == other_list,
        "same object": first is same_list,
        "different objects": first is not other_list,
        "none check": None is None,
    }


# Level 7: Bitwise operators

def bitwise(first, second):
    return {
        "AND": first & second,
        "OR": first | second,
        "XOR": first ^ second,
        "NOT first": ~first,
        "left shift first": first << 1,
        "right shift first": first >> 1,
    }


def is_even_bitwise(number):
    return number & 1 == 0


# Level 8: Precedence

def precedence_examples():
    return {
        "normal order": 2 + 3 * 4,
        "with parentheses": (2 + 3) * 4,
        "power first": 2 ** 3 + 4 * 2 - 1,
        "combined condition": 5 + 2 > 6 and 8 != 0,
    }


# Level 9-10: Real-world combinations and simple calculator

def positive_and_even(number):
    return number > 0 and number % 2 == 0


def divisible_by_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0


def result_summary(marks):
    total = sum(marks)
    average = total / len(marks)
    return {"total": total, "average": average, "pass": all(mark >= 35 for mark in marks)}


def salary_after_raise(salary, percent):
    salary += salary * percent / 100
    return salary


def price_after_discount(price, percent):
    price -= price * percent / 100
    return price


def loan_eligible(salary, age):
    return salary >= 30000 and 21 <= age <= 60


def valid_login(username, password, users):
    return username in users and users[username] == password


def calculator(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            return "Cannot divide by zero"
        return first / second
    if operator == "%":
        if second == 0:
            return "Cannot divide by zero"
        return first % second
    return "Unknown operator"


def main():
    print("Arithmetic:", arithmetic(10, 3))
    print("Assignment steps:", assignment_steps(4))
    print("Compare:", compare(5, 3))
    print("Between 10 and 50:", between_10_and_50(25))
    print("Apple is in fruit list:", is_present("Apple", ["Apple", "Pear"]))
    print("Identity:", identity_examples())
    print("Bitwise:", bitwise(6, 3))
    print("Precedence:", precedence_examples())
    print("Positive and even:", positive_and_even(8))
    print("Calculator:", calculator(7, "*", 6))


if __name__ == "__main__":
    main()
