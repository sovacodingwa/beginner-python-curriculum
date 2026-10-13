# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a smaller number: "))
quotient = number1 // number2
remainder = number1 % number2
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"

animal = input ("What is your favorite animal? ")
color = input ("What is your favorite color? ")
print("A",color,animal,"would be awsome!",)

# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range(11):
    if i % 2 == 0:
        print(i)

# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.

push_ups = int(input("How many push-ups can you do in one day? "))
number_push_ups = push_ups * 7
print("You can do",number_push_ups,"push-ups in a week!")

# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)

for i in range(1, 7):
    print(f"{i} * {i} = {i*i}")