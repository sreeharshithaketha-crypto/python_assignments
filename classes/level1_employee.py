# Q3: Create an Employee class and one employee object.
class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job

employee = Employee("Anu", "Manager")
print(employee.name, employee.job)
