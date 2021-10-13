from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
mtx = [[0] * m for _ in range(n)]
visitied = [[False] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    mtx[r - 1][c - 1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visitied[i][j] = True
    count = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visitied[nx][ny] and mtx[nx][ny] == 1:
                visitied[nx][ny] = True
                q.append([nx, ny])
                count += 1

    return count

result = 0

for i in range(n):
    for j in range(m):
        if not visitied[i][j] and mtx[i][j] == 1:
            result = max(result, bfs(i, j))

print(result)

