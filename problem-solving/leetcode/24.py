class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# 내 풀이
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        temp_list = []

        while head:
            temp_list.append(head.val)
            head = head.next

        for i in range(len(temp_list)):
            index = i + 1
            if index % 2 == 0:
                temp_list[i - 1], temp_list[i] = temp_list[i], temp_list[i - 1]

        head = None
        tail = None

        for val in temp_list:
            if not head:
                head = ListNode(val)
                tail = head
            else:
                tmp = ListNode(val)
                tail.next = tmp
                tail = tail.next

        return head

# 책 풀이
'''    
def swapPairs(self, head: ListNode) -> ListNode:
    node = head

    while node and node.next:
        node.val, node.next.val = node.next.val, node.val
        node = node.next.next

    return head
'''