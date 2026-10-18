age = int(input("How old are you? "))

if age >= 18:
    print("You can vote!")

print("Vote check complete.")

temp = int(input("What's the temperature outside? "))

if temp < 10:
    print("It's cold, wear a jacket.")
else:
    print("No jacket needed.")

day = input("What day of the week is it? ")

if day == "monday":
    print("Ugh, it's Monday.")
elif day == "friday":
    print("Yay, it's almost the weekend")
elif day == "saturday":
    print("It's the weekend!")
elif day == "sunday":
    print("It's the weekend!")
else:
    print("Just a regular weekday.")
print("Day check complete.")

score = int(input("What is your score out of 100? "))

if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A!")
else:
    print("You did not pass")
print("Grading complete.")