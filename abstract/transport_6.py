# Level 6: Real-World Practice - Question 5 (Transport)
# Create an abstract Transport class and implement Bus, Train, Flight, and Cab transportation.
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def travel(self):
        pass

class Bus(Transport):
    def travel(self):
        return "bus"

class Train(Transport):
    def travel(self):
        return "train"

class Flight(Transport):
    def travel(self):
        return "flight"

class Cab(Transport):
    def travel(self):
        return "cab"
