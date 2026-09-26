# Level 1: Basic Abstract Classes - Question 9 (Food)
# Create an abstract class Food with an abstract method prepare(). Implement it using Pizza and Burger.
from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza(Food):
    def prepare(self):
        return "making pizza"

class Burger(Food):
    def prepare(self):
        return "making burger"

if __name__ == "__main__":
    print(Pizza().prepare())
    print(Burger().prepare())
