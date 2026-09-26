# Level 1: Basic Abstract Classes - Question 4 (Employee)
# Create an abstract class Employee with an abstract method work(). Implement it in Developer and Tester.
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        return "coding"

class Tester(Employee):
    def work(self):
        return "testing"

if __name__ == "__main__":
    print(Developer().work())
    print(Tester().work())
