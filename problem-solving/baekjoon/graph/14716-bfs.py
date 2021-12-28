# 실버 1
# 14716. 현수막

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(n)]

q = deque()

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, -1, 1, 1, -1]

def bfs(i, j):
    q.append([i, j])
    mtx[i][j] = 0

    while q:
        x, y = q.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and mtx[nx][ny] == 1:
                q.append([nx, ny])
                mtx[nx][ny] = 0

count = 0

for i in range(n):
    for j in range(m):
        if mtx[i][j] == 1:
            bfs(i, j)
            count += 1

print(count)
