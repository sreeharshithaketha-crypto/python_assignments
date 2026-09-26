try:
    file = open("student.txt", "r")
except FileNotFoundError:
    print("The file was not found.")