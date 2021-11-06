# Easy
# 100. Same Tree

class Solution:
    def isSameTree(self, p, q):
        a = []
        b = []

        def search(node):
            if not node or node.val == None:
                b.append(None)
                return
            b.append(node.val)
            search(node.left)
            search(node.right)

        search(p)

        a = b
        b = []

        search(q)

        return a == b