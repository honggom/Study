# Easy
# 852. Peak Index in a Mountain Array

class Solution:
    def peakIndexInMountainArray(self, arr):
        mx = max(arr)
        return arr.index(mx)