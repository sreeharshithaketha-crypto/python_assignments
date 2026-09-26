subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
try:
    idx = int(input("Enter index (0-4): "))
    print("Selected:", subjects[idx])
except ValueError:
    print("Enter integer index.")
except IndexError:
    print("Index out of range.")
