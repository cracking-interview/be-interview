class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(-1)
    cur = head

    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next

        cur = cur.next

    # last node
    if l1 != None:
        cur.next = l1
    else:
        cur.next = l2
    return head.next