import random
from datetime import datetime

def get_personal_info():
    personal_info = {}
    personal_info["name"] = input(f"Enter your name: ")
    personal_info["age"] = input(f"Enter your age: ")
    personal_info["address"] = input(f"Enter your address: ")
    personal_info["email"] = input(f"Enter your email: ")
    return personal_info

def get_bet_and_numbers():
    while True:
        try:
            bet = int(input(f"Enter your bet (minimum 50): "))
            if bet < 50:
                print("Invalid bet. Minimum bet is 50.")
                continue
            first_number = int(input(f"Enter your first number (1-9): "))
            second_number = int(input(f"Enter your second number (1-9): "))
            if first_number < 1 or first_number > 9 or second_number < 1 or second_number > 9:
                print("Invalid numbers. Numbers must be between 1 and 9.")
                continue
            return bet, first_number, second_number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def generate_numbers():
    return random.randint(1, 9), random.randint(1, 9)

def calculate_winnings(bet, first_number, second_number, winning_number, losing_number):
    winnings = 0
    if first_number == winning_number or second_number == winning_number:
        winnings += bet * 20
    if first_number == winning_number and second_number == losing_number:
        winnings += bet * 100
    return winnings

personal_info = get_personal_info()
bet, first_number, second_number = get_bet_and_numbers()
winning_number, losing_number = generate_numbers()
winnings = calculate_winnings(bet, first_number, second_number, winning_number, losing_number)

print(f"Personal Information: {personal_info}")
print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
print(f"Betting Numbers: {first_number}, {second_number}")
print(f"Winning and Losing Numbers: {winning_number}, {losing_number}")
print(f"Winnings: {winnings}")