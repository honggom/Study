class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        right = len(nums) - 1

        while target - nums[right] not in nums:
            right -= 1
        return [nums.index(target - nums[right]), right]
