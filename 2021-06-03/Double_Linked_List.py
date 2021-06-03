class Node():

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = None
        self.next = None


class DLL():

    def __init__(self, data):
        self.head = Node(data, None, None)
        self.tail = self.head

    def insert(self, data):
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next


dll = DLL(4)
dll.insert(5)
