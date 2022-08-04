nums = [3, 2, 2, 3]
val = 3

answer = []
for i in nums:
    if i != val:
        answer.append(i)

for i in range(len(answer)):
    nums[i] = answer[i]

nums = nums[:len(answer)]
print(len(nums))
