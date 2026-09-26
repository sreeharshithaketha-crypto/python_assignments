# Level 5: Abstract + Concrete Methods - Question 8 (Notification)
# Create an abstract Notification class with an abstract method send() and a normal method display_message().
from abc import ABC, abstractmethod

class Notification(ABC):
    def display_message(self):
        return "msg"

    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self):
        return "email"
