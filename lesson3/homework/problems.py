# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
test1 = int(input("what did you get on your test? "))
test2 = int(input("what did you get on your test? "))
if test1<=50 or test2<=50:
    print("You failed at least one")
else:
    print("you passed both!")

# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = input("did you bring lunch? ")
water = input("did u bring water? ")

if lunch == "yes" and water == "yes":
    print("you are preped")
elif lunch == "yes" or water== "yes":
    print("you are somewhat preped")
else:
    print("you are not preped")

# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
num = int(input("give a num: "))
if num >=1 and num <=10:
    print("in range")
else:
    print("out of range")


# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
score = int(input("test score: "))
if score>90:
    print("A")
elif score >80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
else:
    print("F")

# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1= int(input("give num: "))
num2= int(input("give num: "))
if num1%5 ==0 and num2%2 != 0:
    print("interesting pair")
else:
    print("boring pair") 