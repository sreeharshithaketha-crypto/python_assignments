# Level 5: Abstract + Concrete Methods - Question 2 (Vehicle)
# Create an abstract Vehicle class with an abstract method start() and a normal method display_info().
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def display_info(self):
        return "vehicle info"

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "car start"
