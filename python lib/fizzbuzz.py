class FizzBuzz:
    def __init__(self):
        self.number = 1

    def next(self):
        if self.number % 3 == 0 and self.number % 5 == 0:
            print("FizzBuzz")
        elif self.number % 3 == 0:
            print("Fizz")
        elif self.number % 5 == 0:
            print("Buzz")
        else:
            print(self.number)
        self.number += 1

    def reset(self):
        self.number = 1

# Usage example
fizz_buzz = FizzBuzz()

for _ in range(1, 101):  # Loop through numbers 1 to 100
    fizz_buzz.next()
