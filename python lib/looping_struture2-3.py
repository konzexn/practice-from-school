f = [
    "apple", "banana", "cherry", "durian", "eggplant", "fig", "grape",
    "kiwi", "lemon", "mango", "orange", "pear", "pineapple", "plum",
    "strawberry", "watermelon"
]

while True:
    print("\nMenu:")
    print("1. Display the list of fruits")
    print("2. Check if a fruit is in the list")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nList of fruits:")
        for i, name in enumerate(f, 1):
            print(f"{i}. {name}")
    elif choice == "2":
        fruit_to_check = input("Enter the name of the fruit: ")
        if fruit_to_check in f:
            print(f"{fruit_to_check} is in the list.")
            print(f"Index of {fruit_to_check}: {f.index(fruit_to_check) + 1}")
            print(f"Number of occurrences: {f.count(fruit_to_check)}")
        else:
            print(f"{fruit_to_check} is not in the list.")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
