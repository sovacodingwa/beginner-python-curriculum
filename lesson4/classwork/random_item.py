import random

animals = ["Cat", "dog", "rabbit", "hamster", "parrot"]

length = len(animals)

random_index = random_index = random.randint(0, length - 1)

random_animal = animals[random_index]
print("Random animal:", random_animal)

shortcut_animal = random.choice(animals)
print("Rando choice shortcut:", shortcut_animal)