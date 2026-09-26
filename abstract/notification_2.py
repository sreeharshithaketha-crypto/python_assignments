# Level 2: Multiple Methods - Question 5 (Notification)
# Create an abstract class Notification with abstract methods send() and schedule(). Implement them in Email, SMS, and WhatsApp.
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def schedule(self):
        pass

class Email(Notification):
    def send(self):
        return "email send"
    def schedule(self):
        return "email scheduled"

class SMS(Notification):
    def send(self):
        return "sms send"
    def schedule(self):
        return "sms scheduled"

class WhatsApp(Notification):
    def send(self):
        return "whatsapp send"
    def schedule(self):
        return "whatsapp scheduled"
