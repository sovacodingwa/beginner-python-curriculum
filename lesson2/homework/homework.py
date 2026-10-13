# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the secon number: "))
quotient = num1 // num2 
remainder = num1 % num2
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")


# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
color = input("What is your favorite color? ")
animal =input("What is your favorite animal? ")
print(f"A {"blue"} {"tiger"} would be awesome! ")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range(2, 11, 2):
    print(i)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
daily_push_ups = input("How many push-ups can u do in a day? ")
weekly_push_ups = int(daily_push_ups) * 7
print(f"That means u can do {weekly_push_ups} in a week! ")


# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for i in range(1, 7):
    square = i * i 
    print(f"The square of {i} is {square}")