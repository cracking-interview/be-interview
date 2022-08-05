/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        if (list1 == null) return list2
        if (list2 == null) return list1
        
        val (small, large) = 
            if (list1.`val` < list2.`val`)
                list1 to list2
            else
                list2 to list1
        
        small.next = mergeTwoLists(small.next, large)
        return small
    }
}