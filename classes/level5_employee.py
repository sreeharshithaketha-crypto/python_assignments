# Q2: Use __init__ to initialize employee details.
class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

employee = Employee(1, "Ravi", "IT", 30000)
print(employee.employee_id, employee.name, employee.department, employee.salary)
