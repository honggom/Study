# Easy
# 409. Longest Palindrome

from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        counted = Counter(s).most_common()
        count = 0
        odd = []

        for c in counted:
            if c[1] % 2 == 0:
                count += c[1]
            else:
                odd.append(c[1])

        for i in range(len(odd)):
            if i == 0:
                count += odd[i]
            else:
                count += odd[i] - 1

        return count