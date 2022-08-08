# 27 ms	13.7 MB
def sol(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]

    return nums