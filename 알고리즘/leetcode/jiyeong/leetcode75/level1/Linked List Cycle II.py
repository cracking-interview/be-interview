class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = p2 = head
        while True:
            try:
                p1 = p1.next
                p2 = p2.next.next
            except:
                return
            if p1 is p2:
                p2 = head
                while p1 is not p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
