# 1. Create a list containing 5 tuples, where each tuple contains a student's name and marks. Display all students who scored above 75.
students = [("Asha", 80), ("Ravi", 70), ("Meena", 90), ("John", 65), ("Sara", 78)]
for name, marks in students:
    if marks > 75:
        print(name)
