student = {
"name": "Ravi",
"course": "Python"
}
try:
    print(student["age"])
except KeyError:
    print("The requested key does not exist.")