import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

root = None

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(node):
    if node != None:
        postorder(node.left)
        postorder(node.right)
        print(node.val)

for _ in range(10000):
    try:
        n = int(input())

        if not root:
            root = Node(n)
        else:
            node = root

            while True:
                if n > node.val:
                    if node.right == None:
                        node.right = Node(n)
                        break
                    else:
                        node = node.right
                else:
                    if node.left == None:
                        node.left = Node(n)
                        break
                    else:
                        node = node.left
    except:
        break

postorder(root)