from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(q):
    global result

    while q:
        x, y = q.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and mtx[nx][ny] == 0:
                mtx[nx][ny] = mtx[x][y] + 1
                q.append([nx, ny])

q = deque()

for i in range(n):
    for j in range(m):
        if mtx[i][j] == 1:
            q.append([i, j])

bfs(q)

mx = 0

for i in range(n):
    for j in range(m):
        mx = max(mx, mtx[i][j])

print(mx - 1)