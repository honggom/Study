class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        node_head = head
        node = head

        temp = []
        tail_of_head = None
        head_of_tail = None

        idx = 1

        while node:
            if idx == left - 1:
                tail_of_head = node
            if left <= idx <= right:
                if idx == right:
                    head_of_tail = node.next
                temp.append(node.val)
            idx += 1
            node = node.next
        print(head_of_tail)
        print(tail_of_head)
        print(temp)

        temp.reverse()
        temp_head = None
        temp_tail = None

        for i in range(len(temp)):
            if i == 0:
                temp_head = ListNode(temp[i])
                temp_tail = temp_head
            else:
                temp_tail.next = ListNode(temp[i])
                temp_tail = temp_tail.next

        if temp_head and temp_tail and tail_of_head and head_of_tail:
            tail_of_head.next = temp_head
            temp_tail.next = head_of_tail

        return node_head

n1 = ListNode(3)
n2 = ListNode(5)
n1.next = n2

s = Solution()

l = s.reverseBetween(n1, 1, 2)
while l:
    print(l.val)
    l = l.next