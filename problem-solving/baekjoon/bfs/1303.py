from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mtx = [(list(input().rstrip())) for _ in range(m)]
visitied = [[False] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    count = 1
    visitied[i][j] = True

    while q:
        x, y = q.popleft()
        color = mtx[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < m and 0 <= ny < n and color == mtx[nx][ny] and not visitied[nx][ny]:
                q.append([nx, ny])
                count += 1
                visitied[nx][ny] = True

    return count, color

w = b = 0

for i in range(m):
    for j in range(n):
        if not visitied[i][j]:
            count, color = bfs(i, j)

            if color == "B":
                b += count ** 2
            else:
                w += count ** 2

print(w)
print(b)