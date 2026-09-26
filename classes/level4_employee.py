# Q2: Create an Employee class with a display_salary method.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(self.name, self.salary)

Employee("Ravi", 30000).display_salary()
