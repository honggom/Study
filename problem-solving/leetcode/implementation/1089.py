# Easy
# 1089. Duplicate Zeros

class Solution:
    def duplicateZeros(self, arr):
        jump = False

        for i in range(len(arr)):
            if jump:
                jump = False
                continue
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                del arr[-1]
                jump = True