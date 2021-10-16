import sys
input = sys.stdin.readline

n = int(input())
mtx = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            sys.exit(0)
        if mtx[i][j] + i < n:
            dp[mtx[i][j] + i][j] += dp[i][j]
        if mtx[i][j] + j < n:
            dp[i][mtx[i][j] + j] += dp[i][j]