import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 행렬 수
k = int(input()) # 사과 위치의 개수
mtx = [[0] * n for _ in range(n)]
snake = deque()
snake.append([0, 0])

for _ in range(k):
    apple_pos = list(map(int, input().split()))
    mtx[apple_pos[0] - 1][apple_pos[1] - 1] = -1

l = int(input())
ls = deque()
for _ in range(l):
    ls.append(input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1
nd = d % 4
count = 0

turn = ls.popleft()

def move(x, y):
    if x == n or x == -1 or y == n or y == -1:
        return
    mtx[x][y] = 1

    global count, d, turn

    snake.append([x + dx[nd], y + dy[nd]])

    mtx[x + dx[nd]][y + dy[nd]] = 1

    if mtx[x + dx[nd]][y + dy[nd]] == -1:
        mtx[x + dx[nd]][y + dy[nd]] = 1
    else:
        mtx[x][y] = 0
        snake.popleft()

    count += 1

    if count == int(turn[0]):
        if turn[1] == "D":
            d += 1
            if d == 4:
                d = 0
        else:
            d -= 1
            if d == -1:
                d = 3

        if len(ls) > 1:
            turn = ls.popleft()

    next = snake[-1]
    move(next[0], next[1])

move(0, 0)
print(count)
