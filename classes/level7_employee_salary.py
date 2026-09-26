# Q5: Automatically calculate annual salary from monthly salary.
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

employee = Employee("Ravi", 30000)
print(employee.name, employee.annual_salary())
