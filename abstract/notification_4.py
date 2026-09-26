# Level 4: Polymorphism - Question 5 (Notification)
# Create an abstract Notification class and use polymorphism to send different types of notifications.
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self):
        return "email"

class SMS(Notification):
    def send(self):
        return "sms"
