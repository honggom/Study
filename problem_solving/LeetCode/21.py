class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = []

        while l1:
            l.append(l1.val)
            l1 = l1.next
        while l2:
            l.append(l2.val)
            l2 = l2.next

        tmp = None
        head = None

        for val in sorted(l):
            if not tmp:
                tmp = ListNode(val)
                head = tmp
            else:
                tmp.next = ListNode(val)
                tmp = tmp.next

        return head