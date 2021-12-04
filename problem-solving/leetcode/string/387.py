# Easy
# 387. First Unique Character in a String

from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        counted = Counter(s)

        for k in counted.keys():
            if counted[k] == 1:
                return s.index(k)
        return -1