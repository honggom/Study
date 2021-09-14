from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j, v, arr):
    q = deque()
    q.append([i, j])
    arr[i][j] = 0
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and arr[x][y] == v:
                q.append([x, y])
                arr[x][y] = 0

n = int(input())
rgb = [list(input()) for _ in range(n)]
copy = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if rgb[i][j] == "R" or rgb[i][j] == "G":
            copy[i][j] = 1
        else:
            copy[i][j] = 2

count = 0
count_rg = 0

for i in range(n):
    for j in range(n):
        if rgb[i][j] != 0:
            bfs(i, j, rgb[i][j], rgb)
            count += 1
        if copy[i][j] != 0:
            bfs(i, j, copy[i][j], copy)
            count_rg += 1

print(count, count_rg)