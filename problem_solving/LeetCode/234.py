'''
class Solution:
    def isPalindrome(self, head) -> bool:
        l = []
        if not head:
            return True
        while head:
            l.append(head.val)
            head = head.next
        while len(l) > 1:
            if l.pop(0) != l.pop():
                return False
        return True
'''
class Solution:
    def isPalindrome(self, head) -> bool:
        from collections import deque
        d = deque()

        if not head:
            return True

        while head:
            d.append(head.val)
            head = head.next

        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        return True