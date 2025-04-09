from abc import ABC, abstractmethod

class SQLiteDBABS(ABC):
    def __init__(self, db_name):
        pass

    @abstractmethod
    def create_table(self, table_name, columns):
        pass

    @abstractmethod
    def insert(self, table_name, data):
        pass

    @abstractmethod
    def select(self, table_name, conditions=None):
        pass

    @abstractmethod
    def update(self, table_name, data, conditions):
        pass

    @abstractmethod
    def delete(self, table_name, conditions):
        pass

    @abstractmethod
    def close(self):
        pass




