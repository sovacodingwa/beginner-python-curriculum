animals = ["cat", "dog", "cat", "tiger", "lion"]
print(animals)

num_cats = animals.count("cat")
print(num_cats, "cats")

print("Our algorithm:")

counter = 0
for i in range(len(animals)):
    if animals[i] == "cat":
        counter = counter + 1
print(counter, "cats")

numbers = [14, 1, 50, 4, 20, 12]
counter = 0
for i in range(len(numbers)):
    if numbers[i] > 10:
        counter = counter + 1
print(counter, "numbers above 10")