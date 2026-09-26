# Level 2: Multiple Methods - Question 10 (Report)
# Create an abstract class Report with abstract methods generate() and export(). Implement them using PDFReport and ExcelReport.
from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def export(self):
        pass

class PDFReport(Report):
    def generate(self):
        return "pdf generated"
    def export(self):
        return "pdf exported"

class ExcelReport(Report):
    def generate(self):
        return "excel generated"
    def export(self):
        return "excel exported"
