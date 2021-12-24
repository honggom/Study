# 실버 1
# 11048. 이동하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = mtx[0][0]

for i in range(n):
    for j in range(m):
        left, dig, top = 0, 0, 0

        if j - 1 >= 0:
            left = dp[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0:
            dig = dp[i - 1][j - 1]
        if i - 1 >= 0:
            top = dp[i - 1][j]

        dp[i][j] = max(left, dig, top) + mtx[i][j]

print(dp[n - 1][m - 1])