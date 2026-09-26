# 3. Create a dictionary of employees and their departments. Use sets to find all unique departments.
employees = {"Asha": "IT", "Ravi": "Sales", "Neha": "IT", "Amit": "HR"}
departments = set(employees.values())
print(departments)
