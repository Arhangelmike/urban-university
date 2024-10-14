import sqlite3, random


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS User1(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
#cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON User1 (email)")


#Заполните её 10 записями:
# for i in range(10):
#     cursor.execute("INSERT INTO User1(username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{random.randint(10,99)}", f"{1000}"))


# Обновите balance у каждой 2ой записи начиная с 1ой на 500
#     cursor.execute(f"UPDATE User1 SET balance = {500} where  ID%2=1")


for i in range(11):
    if i == 1 or i == 4 or i == 7 or i == 10:
        cursor.execute(f'DELETE FROM User1 WHERE ID = {i}')

# or cursor.execute(''' DELETE FROM User1 WHERE id%3=1 ''')



connection.commit()
connection.close()