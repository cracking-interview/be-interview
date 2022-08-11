class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head: ListNode) -> ListNode:
        pre = post = head
        while pre and pre.next:
            post = post.next
            pre = pre.next.next
        return post
