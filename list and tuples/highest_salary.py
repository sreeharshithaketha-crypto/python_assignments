# 3. Create a list of tuples containing employee name, designation, and salary. Find the employee with the highest salary.
employees = [("Asha", "Manager", 50000), ("Ravi", "Developer", 60000), ("Meena", "Tester", 45000)]
highest_employee = employees[0]
for employee in employees:
    if employee[2] > highest_employee[2]:
        highest_employee = employee
print(highest_employee)
