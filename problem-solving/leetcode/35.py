class Solution:
    def searchInsert(self, nums, target):
        try:
            return nums.index(target)
        except:
            nums.append(target)
            nums.sort()
            return nums.index(target)
