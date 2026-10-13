fruit = ["banna, apple"]

if "apple" in fruit:
    print("found apple")
else:
    print("no apples found")

print("Our algoirthm:")

found = False 
index = -1

for i in range(len(fruit)): # 0, 1, 2 ... len(fruit) iterations intotal
    if fruit[i] == "apple":
        found = True
        index = 1
        break

if found == True:
    print("Found the apple at", index)
else:
    print("No apples in the list")