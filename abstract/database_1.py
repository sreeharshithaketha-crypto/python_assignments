# Level 1: Basic Abstract Classes - Question 10 (Database)
# Create an abstract class Database with an abstract method connect(). Implement it using MySQLDatabase and PostgreSQLDatabase.
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "mysql connected"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "postgresql connected"

if __name__ == "__main__":
    print(MySQLDatabase().connect())
    print(PostgreSQLDatabase().connect())
