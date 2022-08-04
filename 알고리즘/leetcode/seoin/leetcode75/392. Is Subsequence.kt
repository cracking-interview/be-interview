class Solution {
    fun isSubsequence(s: String, t: String): Boolean {
        if (s.isNullOrBlank()) return true
        if (t.isNullOrBlank()) return false
        
        var flag = true
        var idx = 0
        
        for (i in 0 until s.length) {
            if (idx == t.length) {
                flag = false
                break
            }
            while (idx < t.length) {
                if (s[i] == t[idx]) {
                    flag = true
                    idx++
                    break
                } else {
                    flag = false
                    idx++
                }
            }
        }
        
        return flag
    }
}
