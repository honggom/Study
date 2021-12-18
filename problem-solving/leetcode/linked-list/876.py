# Easy
# 876. Middle of the Linked List

import math

class Solution:
    def middleNode(self, head):
        values = []

        node = head
        node2 = head

        while node:
            values.append(node.val)
            node = node.next

        length = len(values)

        if length % 2 == 0:
            index = int(length / 2)
        else:
            index = math.ceil(int(length / 2))

        for _ in range(index):
            node2 = node2.next
        return node2