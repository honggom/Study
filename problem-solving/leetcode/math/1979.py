# Easy
# 1979. Find Greatest Common Divisor of Array

class Solution:
    def findGCD(self, nums):
        mn = min(nums)
        mx = max(nums)

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        return gcd(mx, mn)