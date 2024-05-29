# Define lists of favorite foods and their ingredients
favorite_foods = ["Pizza", "Sushi", "Chocolate Cake", "Tacos"]
pizza_ingredients = ["Dough", "Tomato sauce", "Cheese", "Pepperoni", "Mushrooms"]
sushi_ingredients = ["Rice", "Nori (Seaweed)", "Fish (Salmon, Tuna, etc.)", "Soy sauce", "Wasabi"]
chocolate_cake_ingredients = ["Flour", "Sugar", "Cocoa powder", "Eggs", "Butter"]
tacos_ingredients = ["Tortillas", "Ground beef", "Lettuce", "Tomatoes", "Cheese", "Salsa"]

# Print the favorite foods and their ingredients
print("My favorite foods:")
for food in favorite_foods:
    print(f"- {food}")

print("\nIngredients:")
print(f"- Pizza: {', '.join(pizza_ingredients)}")
print(f"- Sushi: {', '.join(sushi_ingredients)}")
print(f"- Chocolate Cake: {', '.join(chocolate_cake_ingredients)}")
print(f"- Tacos: {', '.join(tacos_ingredients)}")
