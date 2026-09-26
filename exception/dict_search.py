employee = {"id": 101, "name": "Ramesh", "salary": 30000}
try:
    key = input("Enter key: ")
    print(employee[key])
except KeyError:
    print("The requested employee detail is not available.")
