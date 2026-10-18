import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
brands = ["1","2","3","4"]
print(brands[0])
print(brands[3])
brands.append("5")
print(brands)

# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
numbers = ["1","2",'3','4','5']
print(numbers[2])
numbers.insert(2,"10")
print(numbers)

# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then use a for loop to print each city.
city = ["seattle", "nyc", "bothell"]
length= len(city)
for i in range(length):
    print(city[i])

# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
ex = ["1","2","3","4",'5','6']
length = len(ex)
index = random.randint(0,length-1)
print(ex[index])
ex.pop(3)
print(ex)

# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then use a for loop to print all the names.
names = ["hi","hello", "good morning", "good afternoon", "good evening", "greetings","whats up", "whats good"]
print(names[len(names)//2])
for i in range(len(names)):
    print(names[i])