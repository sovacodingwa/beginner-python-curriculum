numbers = [5,-8,35,-3, 6, 2]
print(numbers)
total= sum(numbers)
print(total)
print("our algorithm")
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
print(total)
total = 0
for i in range(len(numbers)):
    if numbers[i] > 0:
        total = total + numbers[i]
print(total)