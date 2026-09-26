try:
    marks = int(input("Enter marks: "))
    assert 0 <= marks <= 100, "Marks must be between 0 and 100."
except ValueError:
    print("Enter numbers only.")
except AssertionError as error:
    print("Validation error:", error)
else:
    print("Marks accepted.")
