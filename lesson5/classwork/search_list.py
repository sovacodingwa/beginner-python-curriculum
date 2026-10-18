fruit = ["apple", "banana", "apple"]

if "apple" in fruit:
    print("found apple")
else:
    print("no apples found", fruit.index())

print("Our algorithm:")

found = False
index = -1

for i in range(len(fruit)): # 0, 1, 2 ... len(fruit) - 1 = len(fruit) iterations in total
    if fruit[i] == "apple":
        found = True
        index = i
        break

if found == True:
    print("Found the apple at", index)
else:
    print("No apples in the list")
