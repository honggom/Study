# Easy
# 326. Power of Three

class Solution:
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        while n != 1:
            if n / 3 == int(n / 3):
                n = n / 3
            else:
                return False
        return True