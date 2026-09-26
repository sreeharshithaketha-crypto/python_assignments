# Level 1: Basic Abstract Classes - Question 6 (Notification)
# Create an abstract class Notification with an abstract method send(). Implement it using EmailNotification and SMSNotification.
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return "email sent"

class SMSNotification(Notification):
    def send(self):
        return "sms sent"

if __name__ == "__main__":
    print(EmailNotification().send())
    print(SMSNotification().send())
