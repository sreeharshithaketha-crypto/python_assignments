# Level 6: Real-World Practice - Question 4 (UniversityCourse)
# Create an abstract UniversityCourse class and implement Engineering, Medical, and Management courses.
from abc import ABC, abstractmethod

class UniversityCourse(ABC):
    @abstractmethod
    def info(self):
        pass

class Engineering(UniversityCourse):
    def info(self):
        return "eng"

class Medical(UniversityCourse):
    def info(self):
        return "med"

class Management(UniversityCourse):
    def info(self):
        return "mgmt"
