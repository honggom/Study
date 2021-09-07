from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == -1:
                q.append((ny, nx))
                graph[ny][nx] = graph[y][x]+1

n = int(input())
sr, sc, er, ec = map(int, input().split())
graph = [[-1] * n for _ in range(n)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
bfs(sr, sc)

print(graph[er][ec])