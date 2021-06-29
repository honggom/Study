class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        node_head = head
        node = head
        prev = None

        even_head = None
        even_tail = None

        count = 1

        while node:
            if count % 2 == 0:
                if not even_head:
                    prev.next = node.next
                    even_head, even_tail = node, node
                    even_head.next, even_tail.next = None, None
                    node = prev
                else:
                    even_tail.next = node
                    even_tail = even_tail.next
                    prev.next = even_tail.next
                    even_tail.next = None
            else:
                prev = node

            count += 1
            node = node.next

        node_tail = None
        last = node_head
        while node_head:
            node_tail = node_head
            node_head = node_head.next

        node_tail.next = even_head

        return last


