# Problem 1
# Write a function that returns your favorite fruit and print it.
def fruit():
    fav = "mango"
    return fav
print(fruit())


# Problem 2
# Write a function that takes one parameter num.
# The function should return the value of num multiplied by 2.
def number(num):
    num2 = num * 2
    return num2
print(number(10))


# Problem 3
# Create a variable for a book, then print it.
# Modify it inside a function and print it again.
book = "hi"
def books():
    book = "hello"
    return book
print(books())


# Problem 4
# Use a while loop to print the numbers from 1 to 7 (inclusive).
num = 1
while num != 8:
    print(num)
    num += 1


# Problem 5
# Use a while loop to print each element in the list.
items = ["chair", "table", "desk"]
num = 1
index = -1
while num <= len(items):
    
    print(items[index]) 
    index +=1
    num +=1 
    
