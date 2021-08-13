n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]

for i in range(len(nums) - 1):
    dp.append(max(dp[i] + nums[i + 1], nums[i + 1]))
print(dp)
print(max(dp))