class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1 = []
        nums2 = []

        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            l2 = l2.next

        nums1.reverse()
        nums2.reverse()

        n1 = ''.join(map(str, nums1))
        n2 = ''.join(map(str, nums2))

        n = int(n1) + int(n2)
        n = list(str(n))
        n.reverse()

        n = list(map(int, n))
        print(n)

        head = None
        tail = None

        for val in n:
            if not head:
                head = ListNode(val)
                tail = head
            else:
                tmp = ListNode(val)
                tail.next = tmp
                tail = tail.next
        return head
