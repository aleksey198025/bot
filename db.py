import sqlite3


class DataBase:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
        self.create_tables("users")

    def create_tables(self, table_name):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            tg_id INTEGER,
            state TEXT,
            ids TEXT
        )
        ''')
        self.conn.commit()

    def add_user(self, tg_id, state, ids=None):
        self.cursor.execute("INSERT INTO users (tg_id, state, ids) VALUES (?, ?, ?)", (tg_id, state, ids))
        self.conn.commit()

