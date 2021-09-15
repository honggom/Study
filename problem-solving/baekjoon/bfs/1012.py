import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or mtx[i][j] == 0:
        return
    mtx[i][j] = 0

    dfs(i - 1, j)
    dfs(i + 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    mtx = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        mtx[y][x] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if mtx[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)