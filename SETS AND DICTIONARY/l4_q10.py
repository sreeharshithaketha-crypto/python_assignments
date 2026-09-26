# 10. Create a dictionary from two lists: one containing keys and another containing values.
keys = ["name", "age", "course"]
values = ["Asha", 20, "Python"]
student = {}
for index in range(len(keys)):
    student[keys[index]] = values[index]
print(student)
