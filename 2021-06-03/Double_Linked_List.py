class Node():

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLL():

    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


dll = DLL(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
dll.desc()
