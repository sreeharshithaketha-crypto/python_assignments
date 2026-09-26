# Mini Project 2: Simple employee management system.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [Employee("Asha", 30000), Employee("Ravi", 35000)]
for employee in employees:
    print(employee.name, employee.salary)
