try:
    marks = float(input("Enter student marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
except ValueError as error:
    print("Invalid marks:", error)
else:
    if marks >= 35:
        print("Student passed.")
    else:
        print("Student failed.")
