# 4. Create a nested list containing student names and three subject marks. Calculate the total and average marks of every student.
students = [["Asha", 80, 75, 90], ["Ravi", 70, 65, 80]]
for student in students:
    name = student[0]
    total = student[1] + student[2] + student[3]
    average = total / 3
    print(name, total, average)
