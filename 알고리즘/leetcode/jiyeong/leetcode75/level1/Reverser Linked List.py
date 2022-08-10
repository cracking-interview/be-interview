class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sol(head:ListNode) -> ListNode :
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    
    return prev