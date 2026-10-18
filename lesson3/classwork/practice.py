# Problem 1
# Ask the user to enter their height in centimeters.
# Print "Tall" if the height is greater than 170, otherwise print "Short".
height = int(input("how tall r u? cm "))
if height >170:
    print("tall")
else:
    print("short")



# Problem 2
# Ask the user for their age.
# If they are 18 or older, print "Adult", else print "Minor".
age = int(input("age? "))
if age >=18:
    print("adult")
else:
    print("minor")


# Problem 3
# Ask the user to enter a number.
# Print "Fizz" if it is divisible by 3, "Buzz" if divisible by 5,
# print "FizzBuzz" if divisible by both 3 and 5,
# otherwise print the number itself.
num = int(input("give me a number: "))
if num%3 == 0:
    print("fizz")
elif num%5==0:
    print("buzz")
elif num%3 == 0 and num%5 == 0:
    print("fizzbuzz")
else:
    print(num)
# Problem 4
# Ask for age and height.
# If age is at least 10 AND height is at least 120 cm, print "You can ride!"
# Otherwise, print "Sorry, you can't ride."
age = int(input("age? "))
height =int(input("height? "))
if age >= 10 and height >=120:
    print("you can ride!")
else:
    print("you cant ride!")
# Problem 5
# Ask the user for a number.
# If it's divisible by 3 AND (either less than 0 OR greater than 100), print "Weird number!"
# Otherwise, print "Normal number."
num = int(input("give num: "))
if num%3==0 and num<0 or num>100:
    print("weird number!")
else:
    print("normal number")