# Level 5: Abstract + Concrete Methods - Question 10 (Report)
# Create an abstract Report class with an abstract method generate() and a normal method display_report_info().
from abc import ABC, abstractmethod

class Report(ABC):
    def display_report_info(self):
        return "info"

    @abstractmethod
    def generate(self):
        pass

class SimpleReport(Report):
    def generate(self):
        return "generated"
