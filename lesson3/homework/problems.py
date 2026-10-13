# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."

score_1 = int(input("What score did you get on your English test? "))
score_2 = int(input("what score did you get on your math test? "))
if score_1 >= 50 and score_2 >= 50:
    print("You passed both!!! ")
else:
    print("you failed at least one. ")
# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."

lunch = (input("did you bring lunch? (yes/no)" ))
water = (input("did you bring water? (yes/no)" ))
if lunch == "yes" and water == "yes":
    print("you are completely ready!")
elif lunch == "no" and water == "no":
    print("you are not ready.")
else:
    print("you are somewhat ready.")

# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."

number = int(input("enter a whole number: "
""))
if number < 10 and not 0:
    print("out of range")
else:
    print("in range")

# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"

test = int(input("enter test score 0-100 "))
if test >= 90:
    print("grade = A")
elif test <= 89 and test >= 80:
    print("grade = B")
elif test <= 79 and test >= 70:
    print("grade = C")
elif test <= 69 and test >= 60:
    print("grade = D")
else:
    print("grade = F")

# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."

A = int(input("enter a number: "))
B = int(input("enter another number: "))
if A % 5 == 0 and B % 2 != 0:
    print("intresting pair")
else:
    print("plain pair")
print("THE END!:)")