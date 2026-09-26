# Level 1: Basic Abstract Classes - Question 2 (Vehicle)
# Create an abstract class Vehicle with an abstract method start(). Implement it in Car and Bike.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "car started"

class Bike(Vehicle):
    def start(self):
        return "bike started"

if __name__ == "__main__":
    print(Car().start())
    print(Bike().start())
