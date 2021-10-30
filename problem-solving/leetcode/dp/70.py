# Easy
# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2, 3]

        for i in range(2, 45):
            dp.append(dp[i] + dp[i - 1])

        return dp[n - 1]