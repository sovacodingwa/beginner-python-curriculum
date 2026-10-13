animals = ["cat","dog","cat","tiger","lion"]
print(animals)
num_cats = animals.count("cat")
print("Our algorithm")
counter = 0
for i in range (len(animals)):
    if animals[i] == "cat":
        counter = counter+1
    print(counter, "cats")
