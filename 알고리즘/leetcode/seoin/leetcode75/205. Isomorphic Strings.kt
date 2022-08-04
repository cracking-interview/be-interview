class Solution {
    fun isIsomorphic(s: String, t: String): Boolean {
        if (s.length != t.length) return false
        if (s.isNullOrBlank() || t.isNullOrBlank()) return false
        
        val map = HashMap<Any, Any>()
        val set = HashSet<Any>()
        
        for (i in 0 until s.length){
            val x : Char = s[i]
            val y : Char = t[i]
            
            if (map.containsKey(x)) {
                if (map[x] != y) return false
            } else {
                if (set.contains(y)) return false
                map.put(x, y)
                set.add(y)
            }
        }
        return true
    }
}
