class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        self.base = self.root
        while True:
            if data == self.base.data:
                print("중복된 KEY 값")
                break
            elif data > self.base.data:
                if self.base.right is None:
                    self.base.right = Node(data)
                    break
                else:
                    self.base = self.base.right
            else:
                if self.base.left is None:
                    self.base.left = Node(data)
                    break
                else:
                    self.base = self.base.left

    def search(self, data):
        self.base = self.root
        while self.base:
            if self.base.data == data:
                return True
            elif self.base.data > data:
                self.base = self.base.left
            else:
                self.base = self.base.right
        return False

    def remove(self, data):
        '''
        삭제하는 경우는 3가지
        1. 리프 노드(자식이 하나도 없을 경우)를 삭제하는 경우
        2. 자식이 하나인 경우
        3. 자식이 두개인 경우
        '''






b = BinarySearchTree(10)
b.insert(11)
b.insert(9)
b





