total = 0
while True:
    try:
        num = int(input("Enter a number from 1 to 10 (or any non-integer to quit): "))
        if 1 <= num <= 10:
            total += num
            print(f"Current total: {total}")
        else:
            print("Number must be between 1 and 10. Exiting...")
            break
    except ValueError:
        print("Invalid input. Exiting...")
        break
