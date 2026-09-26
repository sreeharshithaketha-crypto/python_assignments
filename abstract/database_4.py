# Level 4: Polymorphism - Question 6 (Database)
# Create an abstract Database class and use polymorphism to connect to different databases.
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        return "mysql"

class MongoDB(Database):
    def connect(self):
        return "mongodb"
