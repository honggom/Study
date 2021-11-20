# Easy
# 389. Find the Difference

class Solution:
    def findTheDifference(self, s, t):
        for c in s:
            t = t.replace(c, "", 1)
        return t