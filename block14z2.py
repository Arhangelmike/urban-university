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


# Заполните её 10 записями:
for i in range(10):
    cursor.execute("INSERT INTO User1(username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{random.randint(10,99)}", f"{1000}"))


# Обновите balance у каждой 2ой записи начиная с 1ой на 500
#     cursor.execute(f"UPDATE User1 SET balance = {500} where  ID%2=1")


# for i in range(11):
#     if i == 1 or i == 4 or i == 7 or i == 10:
#         cursor.execute(f'DELETE FROM User1 WHERE ID = {i}')

# or cursor.execute(''' DELETE FROM User1 WHERE id%3=1 ''')


# cursor.execute("SELECT username, email, age, balance FROM User1 WHERE age != 60")
# datasets = cursor.fetchall()
# for dataset in datasets:
#     print(f'Имя: {dataset[0]} | Почта: {dataset[1]} | Возраст: {dataset[2]} | Баланс: {dataset[3]}')



cursor.execute('DELETE FROM User1 WHERE ID=6')

cursor.execute('SELECT COUNT(*) FROM User1')
total_users = cursor.fetchone()[0]
# print(total_users)

cursor.execute('SELECT SUM(balance) FROM User1')
all_balances = cursor.fetchone()[0]
# print(all_balances)
print(all_balances / total_users)

connection.commit()
connection.close()