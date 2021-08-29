from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            queue.append([i, j])

xx = [1, -1, 0, 0]
yy = [0, 0, 1, -1]

while queue:
    row, col = queue.popleft()

    for k in range(4):
        _row = row + yy[k]
        _col = col + xx[k]

        if 0 <= _row < n and 0 <= _col < m and tomatos[_row][_col] == 0:
            tomatos[_row][_col] = tomatos[row][col] + 1
            queue.append([_row, _col])

result = -2
is_not_grow = False

for tomato_one_line in tomatos:
    for tomato in tomato_one_line:
        if tomato == 0:
            is_not_grow = True
        result = max(result, tomato)

if is_not_grow:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)