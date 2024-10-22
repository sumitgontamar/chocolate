# tests/test_app.py
import unittest
from models import SeasonalFlavor, IngredientInventory, CustomerSuggestion

class TestChocolateHouseApp(unittest.TestCase):

    def test_add_seasonal_flavor(self):
        SeasonalFlavor.add_flavor("Pumpkin Spice", "Fall")
        flavors = SeasonalFlavor.get_flavors()
        self.assertIn(('Pumpkin Spice', 'Fall'), [(f[1], f[2]) for f in flavors])

    def test_add_ingredient(self):
        IngredientInventory.add_ingredient("Cocoa", 50)
        inventory = IngredientInventory.get_inventory()
        self.assertIn(('Cocoa', 50), [(i[1], i[2]) for i in inventory])

    def test_add_customer_suggestion(self):
        CustomerSuggestion.add_suggestion("Mint", "None")
        suggestions = CustomerSuggestion.get_suggestions()
        self.assertIn(('Mint', 'None'), [(s[1], s[2]) for s in suggestions])

if __name__ == '__main__':
    unittest.main()
