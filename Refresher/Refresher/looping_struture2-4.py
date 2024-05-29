class Dish:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

    def display(self):
        return f"{self.name} - {self.price}"
    
    
class Order:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_dish(self, dish):
        if dish.available:
            self.items.append(dish)
            self.total += dish.price
        else:
            print(f"Sorry, {dish.name} is not available.")

    def remove_dish(self, dish):
        if dish in self.items:
            self.items.remove(dish)
            self.total -= dish.price

    def display_order(self):
        for dish in self.items:
            print(dish.display())
        print(f"Total: {self.total}")

class Inventory:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, name, quantity):
        self.ingredients[name] = quantity

    def use_ingredient(self, name, quantity):
        if name in self.ingredients and self.ingredients[name] >= quantity:
            self.ingredients[name] -= quantity
        else:
            print(f"Not enough {name} in inventory.")

class Report:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def popular_dishes(self):
        dish_counts = {}
        for order in self.orders:
            for dish in order.items:
                if dish.name in dish_counts:
                    dish_counts[dish.name] += 1
                else:
                    dish_counts[dish.name] = 1
        return sorted(dish_counts.items(), key=lambda x: x[1], reverse=True)
    
while True:
    print("Welcome to the Restaurant!")
    print("1. Order")
    print("2. Inventory")
    print("3. Report")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        dish1 = Dish("Pasta", 100, True)
        dish2 = Dish("Pizza", 150, True)
        dish3 = Dish("Burger", 80, False)
        dish4 = Dish("Salad", 70, True)
        dish5 = Dish("Steak", 200, True)

        order = Order()
        while True:
            print("Menu:")
            print("1. Pasta")
            print("2. Pizza")
            print("3. Burger")
            print("4. Salad")
            print("5. Steak")
            print("6. Done")
            choice = input("Enter your choice: ")

            if choice == "1":
                order.add_dish(dish1)
            elif choice == "2":
                order.add_dish(dish2)
            elif choice == "3":
                order.add_dish(dish3)
            elif choice == "4":
                order.add_dish(dish4)
            elif choice == "5":
                order.add_dish(dish5)
            elif choice == "6":
                print("Your order:")
                order.display_order()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

    elif choice == "2":
        inventory = Inventory()
        inventory.add_ingredient("Pasta", 10)
        inventory.add_ingredient("Pizza", 20)
        inventory.add_ingredient("Burger", 5)
        inventory.add_ingredient("Salad", 15)
        inventory.add_ingredient("Steak", 8)

        while True:
            print("Inventory:")
            for ingredient, quantity in inventory.ingredients.items():
                print(f"{ingredient}: {quantity}")
            choice = input("Enter 'done' when finished: ")
            if choice == "done":
                break

    elif choice == "3":
        report = Report()
        report.add_order(order)
        print("Popular dishes:")
        popular_dishes = report.popular_dishes()
        for dish, count in popular_dishes:
            print(f"{dish}: {count} orders")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")