# Problem 1
# Search the list and print whether "tiger" is found.
animals = ["cat", "dog", "tiger", "lion"]
if "tiger" in animals:
    print("tiger is in list")


# Problem 2
# Count how many words have length greater than 5.

words = ["python", "cat", "elephant", "dog", "computer"]
count = sum(1 for word in words if len(word) > 5)
print(count)

# Problem 3
# Find and print the sum of all the numbers greater than 25 in the list.

numbers = [10, 32, 27, 8, 50]
total = sum(n for n in numbers if n > 25)
print(total)

# Problem 4
# Find and print the biggest number in the list.

numbers = [12, 7, 33, 5]
biggest = max(numbers)
print(biggest)

# Problem 5
# Find and print the biggest number less than 100 in the list.

numbers = [104, 99, 86, 120, 101]
big = max(n for n in numbers if n < 100)
print(big)