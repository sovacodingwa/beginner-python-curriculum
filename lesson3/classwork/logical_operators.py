age = int(input("How old are you? "))
has_ticket = input("Do you have a movie ticket? (yes/no) ")

if age >= 13 and has_ticket == "yes": # AND: both conditions must be True
    print("You can enter the PG-13 movie.")
else:
    print("Sorry, you can't enter.")

has_pass = input("Do you have a bus pass? (yes/no) ")
has_coins = input("Do you have coins to pay? (yes/no) ")

if has_pass == "yes" or has_coins == "yes": # OR: at least one condition is true
    print("You can ride the bus.")
else:
    print("You can't ride the bus.")

homework_done = input("Did you do your homework? (yes/no) ")

if not homework_done == "yes": # NOT: flips True to False and False to True
    print("Go finish your homework!")
else:
    print("Nice job! You're all done")

is_raining = input("Is it raining? (yes/no) ")
has_umbrella = input("Do you have an umbrella? (yes/no) ")

if is_raining == "yes" and not has_umbrella == "yes":
    print("You get we! Stay inside.")
elif is_raining == "yes" and has_umbrella == "yes":
    print("You're ready to go outside")
else:
    print("No rain; you're good to go!")