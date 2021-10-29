# Easy
# 67. Add Binary

class Solution:
    def addBinary(self, a, b):
        return str(bin(int(int("0b" + a, 2) + int("0b" + b, 2))))[2:]