# Easy
# 1189. Maximum Number of Balloons

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text):
        result = 0

        counted = Counter(text)

        strs = ['b', 'a', 'l', 'l', 'o', 'o', 'n']

        while True:
            for c in strs:
                counted[c] -= 1
                if counted[c] < 0:
                    return result

            result += 1