class Solution:
    def maxSubArray(self, nums):
        dp = [nums[0]]

        for i in range(1, len(nums)):
            dp.append(max(nums[i], dp[i - 1] + nums[i]))
        
        return max(dp)
