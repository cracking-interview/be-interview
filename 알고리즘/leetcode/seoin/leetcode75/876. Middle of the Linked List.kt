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
    fun middleNode(head: ListNode?): ListNode? {
        var slow = head
        var fast = head 
    
        while (fast != null) {
            fast = fast.next
            
            if (fast != null) {
                fast = fast.next
                slow = slow?.next
            }
        }
        
        return slow
    }
}