# Level 4: Polymorphism - Question 9 (Authentication)
# Create an abstract Authentication class and use polymorphism for different login methods.
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

class Password(Authentication):
    def login(self):
        return "password login"

class OTP(Authentication):
    def login(self):
        return "otp login"
