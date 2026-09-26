# 7. Create a dictionary containing 5 students and their marks. Display the topper and lowest scorer.
marks = {"Asha": 85, "Ravi": 72, "Neha": 90, "Amit": 66, "Kiran": 78}
topper = None
lowest = None
for name, score in marks.items():
    if topper is None or score > topper[1]:
        topper = (name, score)
    if lowest is None or score < lowest[1]:
        lowest = (name, score)
print("Topper:", topper)
print("Lowest:", lowest)
