class Solution {
    fun maxProfit(prices: IntArray): Int {
        var max = 0
        var min = prices[0]
 
        for (i in 0 until prices.size){
            if (prices[i] - min > max) {
                max = prices[i] - min
            }
            
            if (prices[i] < min) {
                min = prices[i]
            }
        }
        
        return max
    }
}