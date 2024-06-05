# Base class
class Animal:
    def __init__(self, scientific_name, life_expectancy, species):
        self.__scientific_name = scientific_name
        self.__life_expectancy = life_expectancy
        self.__species = species
        self.__personal_info = {}  # Protected attribute
        self.__unique_actions = []  # Private attribute

    def eat(self):
        return f"{self.__species} is eating."

    def sleep(self):
        return f"{self.__species} is sleeping."

    def set_personal_info(self, info):
        self.__personal_info = info

    def get_personal_info(self):
        return self.__personal_info

    def set_unique_actions(self, actions):
        self.__unique_actions = actions

    def get_unique_actions(self):
        return self.__unique_actions

    def get_scientific_name(self):
        return self.__scientific_name

    def get_life_expectancy(self):
        return self.__life_expectancy

    def get_species(self):
        return self.__species


# Subclasses
class Bird(Animal):
    def __init__(self, scientific_name, life_expectancy):
        super().__init__(scientific_name, life_expectancy, "Bird")
        self.set_personal_info({"habitat": "Forest", "diet": "Insects"})
        self.set_unique_actions(["Chirp"])

    def fly(self):
        return "Bird is flying."


class Wolf(Animal):
    def __init__(self, scientific_name, life_expectancy):
        super().__init__(scientific_name, life_expectancy, "Wolf")
        self.set_personal_info({"habitat": "Forest", "diet": "Meat"})
        self.set_unique_actions(["Howl"])

    def run(self):
        return "Wolf is running."


# Aggregation
class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def display_animals(self):
        for animal in self.__animals:
            print(f"Species: {animal.get_species()}")
            print(f"Scientific Name: {animal.get_scientific_name()}")
            print(f"Life Expectancy: {animal.get_life_expectancy()}")
            print(f"Personal Info: {animal.get_personal_info()}")
            print(f"Unique Actions: {animal.get_unique_actions()}")
            print(f"Common Actions: {animal.eat()}, {animal.sleep()}")
            print("\n")


# Usage
zoo = Zoo()

bird = Bird("Aves", 10)
wolf = Wolf("Canis Lupus", 15)

zoo.add_animal(bird)
zoo.add_animal(wolf)

zoo.display_animals()