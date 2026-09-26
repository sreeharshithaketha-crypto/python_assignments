# Level 5: Abstract + Concrete Methods - Question 9 (Database)
# Create an abstract Database class with an abstract method connect() and a normal method display_database_name().
from abc import ABC, abstractmethod

class Database(ABC):
    def display_database_name(self):
        return "db"

    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        return "mysql"
