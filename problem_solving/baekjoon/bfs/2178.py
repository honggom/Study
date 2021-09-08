from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, list(input().strip()))) for _ in range(n)]
q = deque()
q.append([0, 0])

xx = [1, -1, 0, 0]
yy = [0, 0, 1, -1]

while q:
    row, col = q.popleft()

    for k in range(4):
        _row = row + yy[k]
        _col = col + xx[k]

        if 0 <= _row < n and 0 <= _col < m and miro[_row][_col] == 1:
            miro[_row][_col] = miro[row][col] + 1
            q.append([_row, _col])

print(miro[n - 1][m - 1])