colors = ["red", "green", "blue", "yellow"]

print(colors)

print("First color:", colors[0])
print("Second color:", colors[1])
print("Third color:", colors[2])
print("Fourth color:", colors[3])

# Error: index out of range
# print(colors[10])

colors[0] = "maroon"
print("After edit:", colors)

colors.append("orange")
print("After append:", colors)

colors.insert(2, "purple")
print("After insert at index 2:", colors)

colors.remove("green")
print("After removing 'green':", colors)

# Error: removing item not in list
# colors.remove("pink")

popped_color = colors.pop()
print("poppled color:", popped_color)
print("After pop:", colors)

popped_color_at_index = colors.pop(1)
print("Poped color:", popped_color_at_index)
print("After pop at index 1:", colors)

index_of_blue = colors.index("blue")
print("index of 'blue':", index_of_blue)

# Error: finding index of item not in list
# colors.index("pink")

colors.append("blue")
blue_count = colors.count("blue")
print("Count of 'blue':", blue_count)

colors.sort()
print("After sort:", colors)

colors.reverse()
print("After reverse:", colors)