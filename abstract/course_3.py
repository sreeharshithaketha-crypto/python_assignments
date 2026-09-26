# Level 3: Constructors & Variables - Question 9 (Course)
# Create an abstract class Course with course name and duration. Implement OnlineCourse and OfflineCourse.
from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @abstractmethod
    def start(self):
        pass

class OnlineCourse(Course):
    def start(self):
        return "online start"

class OfflineCourse(Course):
    def start(self):
        return "offline start"
