# Easy
# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums):
        seted = set(nums)
        return len(seted) != len(nums)g