# Mini Project 5: Library Management System
# Build a Library Management System using abstract classes for different types of library items.
from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def title(self):
        pass

class Book(Item):
    def title(self):
        return "book"
