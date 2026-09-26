# Level 2: Multiple Methods - Question 6 (FileHandler)
# Create an abstract class FileHandler with abstract methods read() and write(). Implement them in PDFFile, CSVFile, and ExcelFile.
from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class PDFFile(FileHandler):
    def read(self):
        return "pdf read"
    def write(self):
        return "pdf write"

class CSVFile(FileHandler):
    def read(self):
        return "csv read"
    def write(self):
        return "csv write"

class ExcelFile(FileHandler):
    def read(self):
        return "excel read"
    def write(self):
        return "excel write"
