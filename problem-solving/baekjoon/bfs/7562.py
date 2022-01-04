# 실버 2
# 7562. 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 1, 2]
dy = [-2, -1, 1, 2, -2, -1, 2, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()

        if x == start_i and y == start_j:
            print(mtx[x][y])
            break

        for k in range(8):
            nx = dx[k] + x
            ny = dy[k] + y

            if 0 <= nx < n and 0 <= ny < n and mtx[nx][ny] == 0:
                mtx[nx][ny] = mtx[x][y] + 1
                q.append([nx, ny])

t = int(input())

for _ in range(t):
    n = int(input())
    start_i, start_j = map(int, input().split())
    goal_i, goal_j = map(int, input().split())
    mtx = [[0] * n for _ in range(n)]
    bfs(goal_i, goal_j)