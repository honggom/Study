from collections import deque

mtx = []
max_count = 0
n, m = map(int, input().split())

for i in range(n):
    mtx.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 바이러스를 퍼뜨리고, 안전 영역을 카운트 하는 역할
def bfs():
    global max_count

    copy = [[0] * m for _ in range(n)]
    count = 0
    q = deque()

    for i in range(n):
        for j in range(m):
            copy[i][j] = mtx[i][j]

    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                q.append([i, j])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and copy[nx][ny] == 0:
                copy[nx][ny] = 2
                q.append([nx, ny])

    for i in range(n):
        for j in range(m):
            if copy[i][j] == 0:
                count += 1

    max_count = max(max_count, count)

# 모든 경우의 수로 벽을 세우는 역할
def make_wall(depth):
    if depth == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if mtx[i][j] == 0:
                mtx[i][j] = 1
                make_wall(depth + 1)
                mtx[i][j] = 0

make_wall(0)
print(max_count)