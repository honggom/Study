import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
k = int(input())
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

# 순서대로 위쪽, 오른쪽, 아래쪽, 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1
count = 0

turn = ls.popleft()

def move(x, y):
    global count, d, turn
    mtx[x][y] = 1

    nd = d % 4
    nx = x + dx[nd]
    ny = y + dy[nd]

    if nx == n or nx == -1 or ny == n or ny == -1 or mtx[nx][ny] == 1:
        return

    snake.append([nx, ny])

    if mtx[nx][ny] == -1:
        mtx[nx][ny] = 1
    else:
        tail = snake.popleft()
        mtx[tail[0]][tail[1]] = 0

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

        if len(ls) > 0:
            turn = ls.popleft()

    head = snake[-1]
    move(head[0], head[1])

move(0, 0)
print(count + 1)