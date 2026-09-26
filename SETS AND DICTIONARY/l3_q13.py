# 13. Create a dictionary of employee names and salaries. Calculate the average salary.
salaries = {"Asha": 50000, "Ravi": 60000, "Neha": 70000}
total = 0
for salary in salaries.values():
    total += salary
print(total / len(salaries))
