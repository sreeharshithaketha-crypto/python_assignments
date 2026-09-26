# Q2: Use a class variable company_name for employees.
class Employee:
    company_name = "Good Company"

    def __init__(self, name):
        self.name = name

for employee in [Employee("Asha"), Employee("Ravi")]:
    print(employee.name, employee.company_name)
