# connect to sql DB
import sqlite3


class Connection:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS coffe (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, money FLOAT,
            operation_count INTEGER)''')
        self.conn.commit()

    def insert_data(self, type_value, money, operation_count):
        self.cursor.execute("INSERT INTO coffe (type, money, operation_count) VALUES (?,?,?)",
                            (type_value, money, operation_count))
        self.conn.commit()

    def select_data(self):
        self.cursor.execute("SELECT * FROM coffe")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.conn.commit()

    def update_data(self, id_value, type, money, operation_count):
        self.cursor.execute("UPDATE coffe SET type=?, money=?, operation_count=? WHERE id=?",
                            (type, money, operation_count, id_value))
        self.conn.commit()

    def delete_data(self, id_value):
        self.cursor.execute("DELETE FROM coffe WHERE id=?", (id_value,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
