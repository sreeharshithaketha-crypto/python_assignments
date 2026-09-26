# Mini Project 9: File Processing System
# Build a File Processing System using abstract classes for PDF, CSV, Excel, and JSON file handlers.
from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def process(self):
        pass

class PDF(FileHandler):
    def process(self):
        return "pdf"
