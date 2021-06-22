class Node():

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Double_Linked_List():

    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    # head부터 순차적으로 print
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # head에서부터 순차적으로 검색
    def searchFromHead(self, data):
        node = self.head
        count = 0
        while node:
            if node.data == data:
                print("index is", count)
                return
            count += 1
            node = node.next
        print("not found")

    # tail에서부터 순차적으로 검색
    def searchFromTail(self, data):
        node = self.tail
        count = -1
        while node:
            if node.data == data:
                print("index is", count)
                return
            count += -1
            node = node.prev
        print("not found")

    # data를 가진 node전에(head로부터 가까운 쪽) beforeData를 삽입
    def insertBefore(self, data, beforeData):
        if data == self.head.data:
            node = Node(beforeData)
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev
        else:
            targetNode = self.head
            while targetNode:
                if targetNode.data == data:
                    node = Node(beforeData)
                    node.prev = targetNode.prev
                    node.next = targetNode
                    targetNode.prev.next = node
                    targetNode.prev = node
                    return
                else:
                    targetNode = targetNode.next
            print("data not found")


dll = Double_Linked_List("zero")
dll.insert("one")
dll.insert("two")
dll.insertBefore("two", "bfTwo")
dll.insertBefore("zero", "00")
dll.desc()
