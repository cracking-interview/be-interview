class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val lens = nums.size
        val ans : IntArray = intArrayOf(-1, -1)
        for (i in 0 until lens) {
            for (j in i + 1 until lens) {
                if (nums[i] + nums[j] == target)  {
                    ans[0] = i
                    ans[1] = j
                    break
                }
            }
            if (ans[0] != -1) break
        }
        return ans
    }
}

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val indexMap = mutableMapOf<Int, Int>()
        for (i in nums.indices) {
            val desired = target - nums[i]
            indexMap[desired]?.let {
                return intArrayOf(it, i)
            }
        indexMap[nums[i]] = i
        }

    throw IllegalStateException("The problem should have at least one solution")
    }
}

