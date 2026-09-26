# 4. Create two dictionaries containing student marks for two subjects. Find students who appear in both dictionaries.
maths = {"Asha": 85, "Ravi": 72, "Neha": 90}
science = {"Ravi": 75, "Neha": 88, "Amit": 80}
maths_students = set(maths)
science_students = set(science)
print(maths_students.intersection(science_students))
