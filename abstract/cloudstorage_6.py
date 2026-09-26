# Level 6: Real-World Practice - Question 7 (CloudStorage)
# Create an abstract CloudStorage class and implement GoogleDrive, AWSStorage, and AzureStorage.
from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def store(self):
        pass

class GoogleDrive(CloudStorage):
    def store(self):
        return "gdrive"

class AWSStorage(CloudStorage):
    def store(self):
        return "aws"

class AzureStorage(CloudStorage):
    def store(self):
        return "azure"
