class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return [i, j]