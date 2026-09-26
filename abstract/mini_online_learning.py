# Mini Project 6: Online Learning System
# Build an Online Learning System using abstract classes for different course types.
from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def start(self):
        pass

class OnlineCourse(Course):
    def start(self):
        return "online"
