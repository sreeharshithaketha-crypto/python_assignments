# Q10: Add, remove, search, and display company employees.
class Company:
    def __init__(self):
        self.employees = []

    def add(self, name):
        self.employees.append(name)

    def remove(self, name):
        self.employees.remove(name)

    def search(self, name):
        return name in self.employees

    def display(self):
        print(self.employees)

company = Company()
company.add("Asha")
company.add("Ravi")
print(company.search("Asha"))
company.remove("Ravi")
company.display()
