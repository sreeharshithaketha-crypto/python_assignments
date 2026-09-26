# Level 6: Real-World Practice - Question 10 (Database)
# Create an abstract Database class and implement MySQL, PostgreSQL, MongoDB, and SQLite database classes.
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        return "mysql"

class PostgreSQL(Database):
    def connect(self):
        return "postgresql"

class MongoDB(Database):
    def connect(self):
        return "mongodb"

class SQLite(Database):
    def connect(self):
        return "sqlite"
