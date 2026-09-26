# Level 2: Multiple Methods - Question 9 (Course)
# Create an abstract class Course with abstract methods start_course() and get_duration(). Implement them using OnlineCourse and OfflineCourse.
from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def start_course(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass

class OnlineCourse(Course):
    def start_course(self):
        return "online started"
    def get_duration(self):
        return "4 weeks"

class OfflineCourse(Course):
    def start_course(self):
        return "offline started"
    def get_duration(self):
        return "8 weeks"
