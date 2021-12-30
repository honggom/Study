# 실버 5
# 14916. 거스름돈

import sys

n = int(input())
dp = [sys.maxsize] * 100001
dp[0] = 0
dp[1] = -1
dp[2] = 1
dp[3] = -1
dp[4] = 2

for i in range(5, 100001):
    if dp[i - 5] != -1:
        dp[i] = min(dp[i], dp[i - 5] + 1)
    if dp[i - 2] != -1:
        dp[i] = min(dp[i], dp[i - 2] + 1)
    if dp[i] == sys.maxsize:
        dp[i] = -1

print(dp[n])