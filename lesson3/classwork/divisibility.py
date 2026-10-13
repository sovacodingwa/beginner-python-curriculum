age = int(input("how old are you. "))
has_ticket = input("do you have a ticket? ")
if age >= 13 and has_ticket == "yes":
    print("enter now. ")
else:
    print("leave now. ")
has_pass = input("do you have a pass? ")
has_money = input("do you have money to pay? ")
if has_pass == "yes" or has_money == "yes":
    print("get on the bus now. ")
else:
    print("leave! ")
homework_done = input("Did you do your homework? (yes/no)")
if not homework_done == "yes":
    print("do your homework! ")
else:
    print("have fun! ")

is_raining = input("is it raining? (yes/no) ")
has_umbrella = input("do you have an umbrella? (yes/no) ")
if is_raining == 