class Solution {
    fun pivotIndex(nums: IntArray): Int {
        var arraySum = nums.sum() - nums[0]
        if (arraySum == 0) return 0
        var sum = 0
    
        for (i in 1 until nums.size) {
            arraySum -= nums[i]
            sum += nums[i-1]
            if (sum == arraySum) return i
        }
        return -1
    }
}