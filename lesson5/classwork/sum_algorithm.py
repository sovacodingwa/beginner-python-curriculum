numbers = [5, -8, 35, -3, 6, 2]
print(numbers)

total = sum(numbers)
print("The sun is:", total)

print("Our algorithm")

total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
print("The sun is:", total)

total = 0
for i in range(len(numbers)):
    if numbers[i] > 0:
        total = total + numbers[1]

print("The sun of only postive numbers is:", total)