from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
mtx = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
pivot = -1
result = sys.maxsize

def dfs(i, j):
    if i < 0 or j < 0 or i >= n or j >= n or mtx[i][j] != 1:
        return
    mtx[i][j] = pivot
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        dfs(nx, ny)

def bfs(q, cur):
    global result
    rollback = []
    find_another_map = False

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and mtx[nx][ny] != cur and mtx[nx][ny] < 0:
                result = min(result, mtx[x][y])
                find_another_map = True

            if 0 <= nx < n and 0 <= ny < n and mtx[nx][ny] == 0:
                if mtx[x][y] < 0:
                    mtx[nx][ny] = 1
                    q.append([nx, ny])
                else:
                    mtx[nx][ny] = mtx[x][y] + 1
                    q.append([nx, ny])

                rollback.append([nx, ny])

        # 다른 섬을 찾았다면 while 탈출
        if find_another_map:
            break

    # bfs로 탐색한 경로 다시 0으로 초기화 시키기
    for rb in rollback:
        mtx[rb[0]][rb[1]] = 0

# 섬 분리하기
for i in range(n):
    for j in range(n):
        if mtx[i][j] == 1:
            dfs(i, j)
            pivot -= 1

# 섬 개수만큼 bfs
for i in range(1, abs(pivot) + 1):
    q = deque()

    for j in range(n):
        for k in range(n):
            if mtx[j][k] == -i:
                q.append([j, k])

    bfs(q, -i)

print(result)