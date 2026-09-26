# Level 5: Abstract + Concrete Methods - Question 6 (Course)
# Create an abstract Course class with an abstract method start() and a normal method display_course_details().
from abc import ABC, abstractmethod

class Course(ABC):
    def display_course_details(self):
        return "details"

    @abstractmethod
    def start(self):
        pass

class Online(Course):
    def start(self):
        return "online started"
