# Easy
# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, n1, n2):
        inter = []

        for n in n1:
            if n in n2:
                inter.append(n)
                n2[n2.index(n)] = '*'

        return inter