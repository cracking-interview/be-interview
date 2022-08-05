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
    fun reverseList(head: ListNode?): ListNode? {
        var headNode = head
        
        while (head?.next != null) {
            val a = head
            val b = head.next
            val c = head.next?.next
            
            b?.next = headNode
            a.next = c
            
            headNode = b
        }
        
        return headNode
    }
}