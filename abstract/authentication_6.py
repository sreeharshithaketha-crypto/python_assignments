# Level 6: Real-World Practice - Question 9 (Authentication)
# Create an abstract Authentication class and implement Password, OTP, GoogleLogin, and Biometric authentication.
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

class PasswordAuth(Authentication):
    def login(self):
        return "password"

class OTPAuth(Authentication):
    def login(self):
        return "otp"

class GoogleLogin(Authentication):
    def login(self):
        return "google"

class Biometric(Authentication):
    def login(self):
        return "bio"
