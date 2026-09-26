# Q7: Create three College objects.
class College:
    def __init__(self, name, location, course):
        self.name = name
        self.location = location
        self.course = course

college1 = College("ABC College", "Delhi", "BCA")
college2 = College("City College", "Pune", "BBA")
college3 = College("Green College", "Chennai", "BSc")
print(college1.name, college1.location, college1.course)
print(college2.name, college2.location, college2.course)
print(college3.name, college3.location, college3.course)
