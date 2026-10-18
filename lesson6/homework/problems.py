# Problem 1
# Write a function that returns the number 42 and print the result.
def num():
    return 42
print(num()) 


# Problem 2
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter
print(calculate_perimeter(1, 2))


# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
fruit = "banana"
def fruit():
    fruit = "apple"
    return fruit
print(fruit())


# Problem 4
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
num = 2
while num <= 12:
    print(num)
    num += 2


# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
animals = ["cat", "dog", "rabbit"]
index = 0
while index < len(animals):
    print(animals[index], "is awesome!")
    index += 1
