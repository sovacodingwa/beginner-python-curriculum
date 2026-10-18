# Problem 1
# Search the list and print whether "tiger" is found.
found = False
animals = ["cat", "dog", "tiger", "lion"]
for i in range(len(animals)):
    if animals[i] == "tiger":
        found = True
if found:
    print("Tiger was found")


# Problem 2
# Count how many words have length greater than 5.
words = ["python", "cat", "elephant", "dog", "computer"]
counter = 0
for i in range(len(words)):
    length = len(words[i])
    if length > 5:
        counter +=1 
print(counter)


# Problem 3
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
greater = []
for i in range(len(numbers)):
    if numbers[i] > 25:
        greater.append(numbers[i])
print(sum(greater))


# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
print(max(numbers))


# Problem 5
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
for i in range(len(numbers)):
    if max(numbers)>100:
        numbers.remove(max(numbers))
print(max(numbers))
