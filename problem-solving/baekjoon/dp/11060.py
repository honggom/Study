# 실버 2
# 11060. 점프 점프

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1001] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if i - j <= nums[j]:
            dp[i] = min(dp[i], dp[j] + 1)

if dp[n - 1] > 1000:
    print(-1)
else:
    print(dp[n - 1])