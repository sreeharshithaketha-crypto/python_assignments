# Level 4: Polymorphism - Question 10 (Report)
# Create an abstract Report class and use polymorphism to generate different types of reports.
from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        return "pdf generated"

class ExcelReport(Report):
    def generate(self):
        return "excel generated"
