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
    connection = sqlite3.connect('database_bot.db')
    cursor = connection.cursor()
    check_user = cursor.execute("SELECT * FROM Users1 WHERE id=?", (user_id,))

    if check_user.fetchone() is None:
        cursor.execute(f'''
            INSERT INTO Users1 VALUES('{user_id}', '{username}', '{first_name}', 0)
        ''')
        connection.commit()


def show_users():
    connection = sqlite3.connect('database_bot.db')
    cursor = connection.cursor()
    user_list =  cursor.execute("SELECT * FROM Users")
    message = ''
    for user in user_list:
        message += f"{user[0]} @{user[1]} {user[2]} \n"
    connection.commit()
    return message


def show_stat():
    connection = sqlite3.connect('database_bot.db')
    cursor = connection.cursor()
    count_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()
    connection.commit()
    return count_users[0]

def ad_to_block(input_id):
    connection = sqlite3.connect('database_bot.db')
    cursor = connection.cursor()
    cursor.execute(f"UPDATE USERS set block = ? WHERE id = ?",(1, input_id))
    connection.commit()


def check_block(input_id):
    connection = sqlite3.connect('database_bot.db')
    cursor = connection.cursor()
    users = cursor.execute(f"SELECT block FROM Usrs where id = {user_id}").fetchone()
    connection.commit()
    return users[0]

def remove_block(input_id):
    connection = sqlite3.connect('database_bot.db')
    cursor = connection.cursor()
    cursor.execute(f"UPDATE USERS set block = ? WHERE id = ?",(0, input_id))
    connection.commit()


connection.commit()
connection.close()
