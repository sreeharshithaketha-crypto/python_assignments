class InvalidSalaryError(Exception):
    pass

try:
    salary = float(input("Enter salary: "))
    if salary < 10000:
        raise InvalidSalaryError("Salary is less than ₹10,000")
    print("Salary accepted.")
except InvalidSalaryError as e:
    print("Invalid salary:", e)
