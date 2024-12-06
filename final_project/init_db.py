import json
import sqlite3

db_file = 'db.sqlite'

def initialize_database():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (item_id) REFERENCES items(id)
    )
    ''')

    load_customers_data(cursor)

    load_items_data(cursor)

    conn.commit()
    conn.close()

def load_customers_data(cursor):
    try:
        with open('customers.json', 'r') as file:
            customers = json.load(file)
        for phone, name in customers.items():
            cursor.execute('INSERT INTO customers (name, email) VALUES (?, ?)', (name, phone + "@example.com"))
    except FileNotFoundError:
        print("Error: customers.json file not found.")

def load_items_data(cursor):
    try:
        with open('items.json', 'r') as file:
            items = json.load(file)
        for item_name, details in items.items():
            cursor.execute('INSERT INTO items (name, description, price) VALUES (?, ?, ?)', (item_name, '', details['price']))
    except FileNotFoundError:
        print("Error: items.json file not found.")

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")
