# Level 6: Real-World Practice - Question 8 (Logger)
# Create an abstract Logger class and implement FileLogger, DatabaseLogger, and ConsoleLogger.
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, msg):
        pass

class FileLogger(Logger):
    def log(self,msg):
        return f"file:{msg}"

class DatabaseLogger(Logger):
    def log(self,msg):
        return f"db:{msg}"

class ConsoleLogger(Logger):
    def log(self,msg):
        return f"console:{msg}"
