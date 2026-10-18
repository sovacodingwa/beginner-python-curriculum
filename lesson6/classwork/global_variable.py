pet = "cat"

def show_pet():
    print("The pet is", pet)

show_pet()

# def adpot_dog():
# print("Old pet is", pet)
# pet = dog()

#adpot_dog()

def adpot_parrot():
    global pet
    pet = "parrot"

adpot_parrot()
show_pet()