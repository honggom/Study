# Easy
# 66. Plus One

class Solution:
    def plusOne(self, digits):
        num = "".join(map(str, digits))
        result = list(map(int, list(str(int(num) + 1))))
        return result