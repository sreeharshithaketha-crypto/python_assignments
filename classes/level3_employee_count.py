# Q8: Use company_name and employee_count class variables.
class Employee:
    company_name = "Tech Ltd"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

Employee("Asha")
Employee("Ravi")
print(Employee.company_name)
print(Employee.employee_count)
