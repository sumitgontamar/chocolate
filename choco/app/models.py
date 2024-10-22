# models.py
from db import get_db

class SeasonalFlavor:
    @staticmethod
    def add_flavor(name, season):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO seasonal_flavors (name, season) VALUES (?, ?)', (name, season))
        conn.commit()
        conn.close()

    @staticmethod
    def get_flavors():
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM seasonal_flavors')
        flavors = cursor.fetchall()
        conn.close()
        return flavors

class IngredientInventory:
    @staticmethod
    def add_ingredient(ingredient, quantity):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ingredient_inventory (ingredient, quantity) VALUES (?, ?)', (ingredient, quantity))
        conn.commit()
        conn.close()

    @staticmethod
    def get_inventory():
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ingredient_inventory')
        inventory = cursor.fetchall()
        conn.close()
        return inventory

class CustomerSuggestion:
    @staticmethod
    def add_suggestion(flavor_suggestion, allergy_concern):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customer_suggestions (flavor_suggestion, allergy_concern) VALUES (?, ?)', (flavor_suggestion, allergy_concern))
        conn.commit()
        conn.close()

    @staticmethod
    def get_suggestions():
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customer_suggestions')
        suggestions = cursor.fetchall()
        conn.close()
        return suggestions
