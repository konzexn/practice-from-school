food = {
    "Adobo": ["pork","soy sauce","vinegar","garlic","onion","bay leaves","pepper corns","sugar","water","salt","oil"],
    "Sinigang": ["pork","tamarind","water","onion","garlic","tomato","radish","string beans","eggplant","salt","pepper"]
}

personal_info = {
    "name": "erwin",
    "age": 29,
    "address": "Panay",
    "email": "konzexn@gmail.com"
}

def display_personal_info():
    print(f"Name: {personal_info['name']}")
    print(f"Age: {personal_info['age']}")
    print(f"Address: {personal_info['address']}")
    print(f"Email: {personal_info['email']}")

display_personal_info()

while True:
    user_response = input("what to food to display? Adobo or Sinigang : ")
    if user_response in food:
        for ingredient in food[user_response]:
            print(ingredient)
        break
    else:
        print("Invalid input. Please enter 'Adobo' or 'Sinigang'.")