personal_info = {
    "name": "erwin",
    "age": 29,
    "address": "Panay",
    "email": "konzexn@gmail.com"
}

functionalities = {
    "1": "Display personal information",
    "2": "Search personal information",
    "3": "Update personal information",
    "4": "Delete personal information",
    "5": "Exit"
}

def display_personal_info():
    print(f"Name: {personal_info['name']}")
    print(f"Age: {personal_info['age']}")
    print(f"Address: {personal_info['address']}")
    print(f"Email: {personal_info['email']}")

def search_personal_info():
    search_key = input("Enter the key you want to search: ")
    if search_key in personal_info:
        print(f"{search_key}: {personal_info[search_key]}")
    else:
        print(f"{search_key} not found.")

def update_personal_info():
    update_key = input("Enter the key you want to update: ")
    if update_key in personal_info:
        personal_info[update_key] = input(f"Enter new {update_key}: ")
        print("Personal information updated.")
    else:
        print(f"{update_key} not found.")

def delete_personal_info():
    delete_key = input("Enter the key you want to delete: ")
    if delete_key in personal_info:
        del personal_info[delete_key]
        print("Personal information deleted.")
    else:
        print(f"{delete_key} not found.")

while True:
    print("\nAvailable functionalities:")
    for key, value in functionalities.items():
        print(f"{key}. {value}")

    choice = input("Enter your choice: ")

    if choice in functionalities:
        if choice == "1":
            display_personal_info()
        elif choice == "2":
            search_personal_info()
        elif choice == "3":
            update_personal_info()
        elif choice == "4":
            delete_personal_info()
        elif choice == "5":
            break
    else:
        print("Invalid choice. Please try again.")
