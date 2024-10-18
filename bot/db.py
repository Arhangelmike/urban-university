import sqlite3


connection = sqlite3.connect('database_bot.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users1(
id INT PRIMARY KEY,
username TEXT,
first_name TEXT,
block INT
);
''')
# cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON User1 (email)")
def add_user(user_id, username, first_name):
    check_user = cursor.execute("SELECT * FROM Users1 WHERE id=?", (user_id,))

    if check_user.fetchone() is None:
        cursor.execute(f'''
            INSERT INTO Users1 VALUES('{user_id}', '{username}', '{first_name}', 0)
        ''')

connection.commit()
connection.close()
