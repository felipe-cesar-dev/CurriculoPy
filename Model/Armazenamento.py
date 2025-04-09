import sqlite3

from Model.ArmazenamentoABS import SQLiteDBABS


class SQLiteDB(SQLiteDBABS):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert(self, table_name, data):
        query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(data))})"
        self.cursor.execute(query, data)
        self.conn.commit()

    def select(self, table_name, conditions=None):
        if conditions:
            query = f"SELECT * FROM {table_name} WHERE {conditions}"
        else:
            query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table_name, data, conditions):
        query = f"UPDATE {table_name} SET {', '.join([f'{key} = ?' for key in data.keys()])} WHERE {conditions}"
        self.cursor.execute(query, list(data.values()))
        self.conn.commit()

    def delete(self, table_name, conditions):
        query = f"DELETE FROM {table_name} WHERE {conditions}"
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()




