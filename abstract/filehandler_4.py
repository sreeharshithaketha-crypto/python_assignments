# Level 4: Polymorphism - Question 7 (FileHandler)
# Create an abstract FileHandler class and use polymorphism to read different file types.
from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

class PDF(FileHandler):
    def read(self):
        return "read pdf"

class CSV(FileHandler):
    def read(self):
        return "read csv"
