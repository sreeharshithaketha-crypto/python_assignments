# Mini Project 10: Complete OOP Demonstration
# Build a complete OOP project demonstrating abstract classes, abstract methods, inheritance, polymorphism, constructors, instance variables, and concrete methods.
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def do(self):
        pass

class Impl(Base):
    def do(self):
        return "done"
