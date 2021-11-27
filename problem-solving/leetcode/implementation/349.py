# Easy
# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, n1, n2):
        result = set()

        for v in set(n1):
            if v in set(n2):
                result.add(v)

        return result