from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        nums = Counter(nums).most_common(k)
        rtn = []
        for n in nums:
            rtn.append(n[0])
        return rtn