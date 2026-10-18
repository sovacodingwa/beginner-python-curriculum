# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
score1 = float(input("Enter the first test score:"))
score2 = float(input("Enter the second test score:"))
if score1 >= 50 and score2 >= 50:
    print("You passed both!")
else:
    print("You failed least one.")


# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
brought_lunch = input("Did you bring lunch? (yes/no):").strip().lower()
brought_water = input("Did you broing water? (yes/no):").strip().lower()
if brought_lunch == "yes" and brought_water == "yes":
    print("You're fully ready!")
elif brought_lunch == "yes" or brought_water == "yes":
    print("You're somewhat ready.")
else:
    print("You're not ready..")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
user_input = input("Please enter a number: ")
number = float(user_input)
if 1 <= number <= 10:
    print("In range.")
else:
    print("Out of range.")
 



# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
user_input = input("Enter a test score (0-100): ")
score = float(user_input)
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Below B")



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter second number: "))
condition_1 = (num1 % 5 == 0) and (num2 % 2 != 0)
condition_2 =(num2 % 5 == 0)  and (num1 % 2 != 0)
if condition_1 or condition_2:
    print("Interesting pair!")
else:
    print("Plain pair")