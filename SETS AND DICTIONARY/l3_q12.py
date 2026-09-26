# 12. Create a dictionary of student names and marks. Find the student with the highest marks without using max().
marks = {"Asha": 85, "Ravi": 72, "Neha": 90}
highest_name = None
highest_marks = None
for name, score in marks.items():
    if highest_marks is None or score > highest_marks:
        highest_name = name
        highest_marks = score
print(highest_name, highest_marks)
