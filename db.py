import sqlite3


connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS User1(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON User1 (email)")
connection.commit()
connection.close()
