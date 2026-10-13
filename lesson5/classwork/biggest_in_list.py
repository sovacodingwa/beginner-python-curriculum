print("lesson 5 classwork ")
fruits = ["banana","apple"]
if "apple" in fruits:
    print("found apple")
else:
    print("no apples hear")
print("our alogoirthm:")
found = True
index = -1
for i in range(len(fruits)):
    if fruits[i] == "apple":
        found = True
        index = i
        break
if found == True:
    print("found the apple at",index)
else:
    print("no apples in the list")
    print("switch with search_list")