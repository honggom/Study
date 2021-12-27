# 실버 1
# 1149. RGB거리

import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(rgb[i][j] + dp[i - 1][j + 1], rgb[i][j] + dp[i - 1][j + 2])
        elif j == 1:
            dp[i][j] = min(rgb[i][j] + dp[i - 1][j - 1], rgb[i][j] + dp[i - 1][j + 1])
        else:
            dp[i][j] = min(rgb[i][j] + dp[i - 1][j - 2], rgb[i][j] + dp[i - 1][j - 1])

print(min(dp[n - 1]))