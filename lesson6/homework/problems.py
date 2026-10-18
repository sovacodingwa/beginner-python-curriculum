# Problem 1
# Write a function that returns the number 42 and print the result.
def get_answer():
    return 42
print(get_answer())
# Problem 2
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).
def calculate_perimeter(length, width):
    return 2 * (length + width)
result = calculate_perimeter(5, 10)
print(result)

# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
fruit = "Apple"
print("Original fruit:", fruit)
def change_fruit():
    global fruit
    fruit = "Mango"
change_fruit()
print("Modified fruit:", fruit)
# Problem 4
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
number = 2
while number <= 12:
    print(number)
    number += 2
# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
animals = ["Dolphin", "Cheetah", "Owl"]
index = 0
while index < len(animals):
    print(animals[index] + " is awsome!")
    index += 1 