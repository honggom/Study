t = int(input())
nums = [list(map(int, input().split())) for _ in range(t)]
dp = []

for n in nums:
    dp.append([0] * len(n))

dp[0][0] = nums[0][0]

for i in range(1, t):
    for j in range(len(nums[i])):
        if j == 0:
            dp[i][j] = max(dp[i][j], nums[i][j] + dp[i - 1][j])
        elif j == len(nums[i]) - 1:
            dp[i][j] = max(dp[i][j], nums[i][j] + dp[i - 1][j - 1])
        else:
            dp[i][j] = max(dp[i][j], nums[i][j] + dp[i - 1][j], nums[i][j] + dp[i - 1][j - 1])

print(max(dp[t - 1]))