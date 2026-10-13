colors = ["red", "green", "blue", "yellow"]

print(colors)

print("First coloor:", colors[0])
print("Second color:", colors[1])
print("Third  color:", colors[2])
print("Fourth color:", colors[3])

# Error: index out of range 
# print(colors[10])

colors[0] = "maroon"
print("After edit:", colors)

colors.append("orange")
print("After append", colors)

colors.insert(2,"purple")
print("After insert at index 2:",colors)


