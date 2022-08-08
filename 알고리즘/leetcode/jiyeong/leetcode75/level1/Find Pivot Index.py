#	119 ms	14.5 MB
def sol(nums):
    right = [0]*len(nums)
    left = [0]*len(nums)
    right[0] = sum(nums) - nums[0]
    if left[0] == right[0]:
        return 0
    for i in range(1, len(nums)):
        left[i] = left[i-1]+nums[i-1]
        right[i] = right[i-1]-nums[i]
        if left[i] == right[i]:
            return i
    else:
        return -1