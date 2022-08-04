nums = [-1, 0, 0, 0, 0, 3, 3]


i = 0
for j in range(len(nums)):
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]

nums = nums[:i+1]

print(i+1)
