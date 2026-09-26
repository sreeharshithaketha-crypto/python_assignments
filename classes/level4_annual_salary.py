# Q9: Calculate an employee annual salary.
class Employee:
    def annual_salary(self, monthly_salary):
        return monthly_salary * 12

employee = Employee()
print(employee.annual_salary(30000))
