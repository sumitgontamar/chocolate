# db.py
import sqlite3

def get_db():
    conn = sqlite3.connect('chocolate_house.db')
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Create tables for seasonal flavors, ingredient inventory, and customer suggestions
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        season TEXT NOT NULL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
                        id INTEGER PRIMARY KEY,
                        ingredient TEXT NOT NULL,
                        quantity INTEGER NOT NULL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                        id INTEGER PRIMARY KEY,
                        flavor_suggestion TEXT NOT NULL,
                        allergy_concern TEXT
                      )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
