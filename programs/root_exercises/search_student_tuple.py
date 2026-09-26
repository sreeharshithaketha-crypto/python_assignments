# 10. Create a list of student tuples and search for a student by name.
students = [("Asha", 80), ("Ravi", 70), ("Meena", 90)]
search_name = "Ravi"
for student in students:
    if student[0] == search_name:
        print(student)
