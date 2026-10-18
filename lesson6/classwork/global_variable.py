pet = "cat"

def show_pet():
    print("The pet is", pet)

show_pet()

# def adopt_dog():
#   print("Old pet is", pet)
#  pet = "dog"

# adopt_dog()

def adopt_parrot():
    global pet
    pet = "parrot"

adopt_parrot()
show_pet()
