# connect to sql DB
import sqlite3


class Connection:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER,
            gender TEXT)''')
        self.conn.commit()

    def insert_data(self, name, age, gender):
        self.cursor.execute("INSERT INTO users (name, age, gender) VALUES (?,?,?)", (name, age, gender))
        self.conn.commit()

    def select_data(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.conn.commit()

    def update_data(self, id, name, age, gender):
        self.cursor.execute("UPDATE users SET name=?, age=?, gender=? WHERE id=?", (name, age, gender, id))
        self.conn.commit()

    def delete_data(self, id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
