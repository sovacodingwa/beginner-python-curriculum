nums = [1, 2, 3]
print(nums)

biggest_item = max(nums)
smallest_item = min(nums)

print("The biggest item:", biggest_item)
print("The smallest number:", smallest_item)

print("Our algorithm")

biggest = nums[0]
for i in range(len(nums)):
    if nums[i] > biggest:
        biggest = nums [i]

print("The biggest item:", biggest)