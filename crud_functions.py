import sqlite3
connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

def get_all_products():
    cursor.execute(" SELECT * FROM Products")
    products = cursor.fetchall()
    return products

def add_product(title, description, price):
    initiate_db()
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (title, description, price))


connection.commit()
connection.close()

add_product('Product1', '1', 100)
add_product('Product2', '2', 200)
add_product('Product3', '3', 300)
add_product('Product4', '4', 400)