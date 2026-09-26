# Q2: Create five Employee objects with instance variables.
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employees = [Employee("A", "IT", 30000), Employee("B", "HR", 28000), Employee("C", "Sales", 25000), Employee("D", "IT", 32000), Employee("E", "Admin", 22000)]
for employee in employees:
    print(employee.name, employee.department, employee.salary)
