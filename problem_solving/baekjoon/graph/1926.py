import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count, mx = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    mx = 1
    while q:
        visited[x][y] = True
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                mx += 1
                q.append([nx, ny])
                visited[nx][ny] = True

    return mx


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            mx = max(mx, bfs(i, j))
            count += 1

print(count)
print(mx)