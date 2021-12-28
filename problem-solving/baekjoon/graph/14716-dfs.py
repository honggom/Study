# 실버 1
# 14716. 현수막

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(n)]

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or mtx[i][j] == 0:
        return
    mtx[i][j] = 0

    dfs(i - 1, j)
    dfs(i, j - 1)
    dfs(i + 1, j)
    dfs(i, j + 1)
    dfs(i - 1, j - 1)
    dfs(i + 1, j + 1)
    dfs(i - 1, j + 1)
    dfs(i + 1, j - 1)


count = 0

for i in range(n):
    for j in range(m):
        if mtx[i][j] == 1:
            dfs(i, j)
            count += 1

print(count)