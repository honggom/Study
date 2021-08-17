n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i, -1, -1):
        if nums[i] < nums[j]:
            dp[i] = max(1 + dp[j], dp[i])

print(max(dp))