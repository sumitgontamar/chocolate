# main.py
from models import SeasonalFlavor, IngredientInventory, CustomerSuggestion

def main_menu():
    while True:
        print("Chocolate House Management")
        print("1. Add Seasonal Flavor")
        print("2. View Seasonal Flavors")
        print("3. Add Ingredient to Inventory")
        print("4. View Ingredient Inventory")
        print("5. Add Customer Flavor Suggestion")
        print("6. View Customer Suggestions")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter flavor name: ")
            season = input("Enter season: ")
            SeasonalFlavor.add_flavor(name, season)
            print("Flavor added successfully!")
        elif choice == '2':
            flavors = SeasonalFlavor.get_flavors()
            print("Seasonal Flavors:")
            for flavor in flavors:
                print(f"Name: {flavor[1]}, Season: {flavor[2]}")
        elif choice == '3':
            ingredient = input("Enter ingredient: ")
            quantity = int(input("Enter quantity: "))
            IngredientInventory.add_ingredient(ingredient, quantity)
            print("Ingredient added successfully!")
        elif choice == '4':
            inventory = IngredientInventory.get_inventory()
            print("Ingredient Inventory:")
            for item in inventory:
                print(f"Ingredient: {item[1]}, Quantity: {item[2]}")
        elif choice == '5':
            suggestion = input("Enter flavor suggestion: ")
            allergy = input("Any allergy concerns? (Optional): ")
            CustomerSuggestion.add_suggestion(suggestion, allergy)
            print("Suggestion added successfully!")
        elif choice == '6':
            suggestions = CustomerSuggestion.get_suggestions()
            print("Customer Suggestions:")
            for suggestion in suggestions:
                print(f"Flavor Suggestion: {suggestion[1]}, Allergy Concern: {suggestion[2]}")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main_menu()
