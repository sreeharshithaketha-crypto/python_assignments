# 3. Create a dictionary containing employee names and salaries. Display employees earning more than Rs. 50,000.
salaries = {"Asha": 50000, "Ravi": 60000, "Neha": 75000}
for name, salary in salaries.items():
    if salary > 50000:
        print(name)
