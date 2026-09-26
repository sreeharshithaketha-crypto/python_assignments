# Q10: Use institute_name and course instance variables.
class Course:
    institute_name = "Skill Institute"

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

course = Course("Python", "3 months")
print(course.institute_name, course.course_name, course.duration)
