# Easy
# 136. Single Number

import collections

class Solution:
    def singleNumber(self, nums):
        counted = collections.Counter(nums)

        for k, v in counted.items():
            if v == 1:
                return k