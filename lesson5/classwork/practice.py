# Problem 1
# Search the list and print whether "banana" is found.
fruits = ["apple", "orange", "banana", "grape"]
found = False
for i in range(len(fruits)):
    if fruits[i]== "banana":
        found= True
        index = i
        break
print(index)


# Problem 2
# Count how many numbers are greater than 10 in the list.
found = 0
numbers = [4, 18, 2, 30, 7, 12]
for i in range(len(numbers)):
    if numbers[i] >10:
        found +=1
    break
print(found)

# Problem 3
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]
print(sum(numbers))

# Problem 4
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0] 
print(max(numbers))


# Problem 5
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]
evens = []

for i in range(len(numbers)):
    if numbers[i-1] % 2 ==0 :
        evens.append(numbers[i-1])
print(sum(evens))
