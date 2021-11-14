# Easy
# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n == 0:
            return False

        while n != 1:
            if n / 2 == int(n / 2):
                n = n / 2
            else:
                return False
        return True