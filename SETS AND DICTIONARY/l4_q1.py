# 1. Create a dictionary of student marks and print students who scored above 75.
marks = {"Asha": 85, "Ravi": 72, "Neha": 90}
for name, score in marks.items():
    if score > 75:
        print(name)
