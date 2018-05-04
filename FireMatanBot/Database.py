import sqlite3


class Database:

    def __init__(self):
        self.db = sqlite3.connect('mydb')
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute('''CREATE TABLE user(chat_id INTEGER PRIMARY KEY, feuerwehr TEXT)''')
        except sqlite3.OperationalError:
            print('Table already exists!')

    def insert(self, chat_id, feuerwehr):
        self.cursor.execute('''INSERT INTO user(chat_id, feuerwehr)VALUES(?, ?)''', (chat_id, feuerwehr))
        self.db.commit()
        print("Insert", chat_id, feuerwehr)

    def update(self, chat_id, feuerwehr):
        self.cursor.execute('''UPDATE user SET feuerwehr=? WHERE chat_id=?''', (feuerwehr, chat_id))
        self.db.commit()
        print("Update", chat_id, feuerwehr)

    def get_feuerwehr(self, chat_id):
        self.cursor.execute('''SELECT feuerwehr FROM user WHERE chat_id=? ''', (chat_id,))
        return self.cursor.fetchone()

    def get_id(self, feuerwehr):
        self.cursor.execute('''SELECT chat_id FROM user WHERE feuerwehr=? ''', (feuerwehr,))
        return self.cursor.fetchall()

    def print_items(self):
        self.cursor.execute('''SELECT * FROM user''')
        print(self.cursor.fetchall())