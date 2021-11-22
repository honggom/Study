# Easy
# 342. Power of Four

class Solution:
    def isPowerOfFour(self, n):
        if n == 0:
            return False

        while n != 1:
            if n / 4 == int(n / 4):
                n = int(n / 4)
            else:
                return False

        return True