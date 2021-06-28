class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        t = None
        p = None
        while head:
            if not p:
                p = ListNode(head.val)
                t = p
            else:
                p = ListNode(head.val)
                p.next = t
                t = p
            head = head.next
        return p