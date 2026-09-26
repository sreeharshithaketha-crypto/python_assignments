marks=int(input("enter marks"))
if marks>=75 and marks<=100:
    print("student passed in first class with distinction")
elif marks>=55 and marks<=74:
    print("student passed in second class")
elif marks>=35 and marks<=54:
    print("student passed in third class")
else:
    print("student failed the exams")