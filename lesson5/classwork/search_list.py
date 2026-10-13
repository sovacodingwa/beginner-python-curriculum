nums = [1,2,3]
print(nums)
biggest_num = max(nums)
smallest_num = min(nums)
print(biggest_num)
print(smallest_num)
print("our algorithm:")
biggest = nums[0]
for i in range (len(nums)):
    if nums[i] > biggest:
        biggest = nums[i]
    print(biggest)
    print("switch with biggest_in_list")
    print(":)")