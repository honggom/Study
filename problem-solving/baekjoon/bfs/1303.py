from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mtx = [(list(input().rstrip())) for _ in range(m)]
visitied = [[False] * n for _ in range(m)]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    count = 1

    while q:
        x, y = q.popleft()
        color = mtx[x][y]
        visitied[x][y] = True

        if 0 <= x + 1 < m and 0 <= y < n and color == mtx[x + 1][y] and not visitied[x + 1][y]:
            q.append([x + 1, y])
            count += 1
            visitied[x + 1][y] = True
        if 0 <= x - 1 < m and 0 <= y < n and color == mtx[x - 1][y] and not visitied[x - 1][y]:
            q.append([x - 1, y])
            count += 1
            visitied[x - 1][y] = True
        if 0 <= x < m and 0 <= y + 1 < n and color == mtx[x][y + 1] and not visitied[x][y + 1]:
            q.append([x, y + 1])
            count += 1
            visitied[x][y + 1] = True
        if 0 <= x < m and 0 <= y - 1 < n and color == mtx[x][y - 1] and not visitied[x][y - 1]:
            q.append([x, y - 1])
            count += 1
            visitied[x][y - 1] = True

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