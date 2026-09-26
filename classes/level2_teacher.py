# Q9: Create multiple Teacher objects.
class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

teachers = [Teacher("Mr. Kumar", "Math", 5), Teacher("Ms. Sara", "English", 3)]
for teacher in teachers:
    print(teacher.name, teacher.subject, teacher.experience)
