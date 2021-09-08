import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(i, j):
    if i < 0 or j < 0 or i >= h or j >= w or mtx[i][j] == 0:
        return

    mtx[i][j] = 0

    dfs(i + 1, j)
    dfs(i, j + 1)
    dfs(i - 1, j)
    dfs(i, j - 1)
    dfs(i - 1, j - 1)
    dfs(i + 1, j + 1)
    dfs(i + 1, j - 1)
    dfs(i - 1, j + 1)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        sys.exit(0)

    lands = 0
    mtx = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if mtx[i][j] == 1:
                dfs(i, j)
                lands += 1

    print(lands)
