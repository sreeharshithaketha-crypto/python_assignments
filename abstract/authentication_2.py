# Level 2: Multiple Methods - Question 7 (Authentication)
# Create an abstract class Authentication with abstract methods login() and logout(). Implement them using PasswordAuth and OTPAuth.
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class PasswordAuth(Authentication):
    def login(self):
        return "password login"
    def logout(self):
        return "password logout"

class OTPAuth(Authentication):
    def login(self):
        return "otp login"
    def logout(self):
        return "otp logout"
