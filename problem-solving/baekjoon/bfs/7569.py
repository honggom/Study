import sys
from collections import deque
input = sys.stdin.readline

q = deque()

def bfs():
    global result

    while q:
        qh, qn, qm = q.popleft()

        for d in range(6):
            nh = qh + dh[d]
            nn = qn + dn[d]
            nm = qm + dm[d]

            if 0 <= nh < h and 0 <= nn < n and 0 <= nm < m and tmts[nh][nn][nm] == 0:
                tmts[nh][nn][nm] = tmts[qh][qn][qm] + 1
                result = max(tmts[qh][qn][qm] + 1, result)
                q.append([nh, nn, nm])

dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, 0, 0, -1, 1]
dm = [0, 0, -1, 1, 0, 0]

m, n, h = map(int, input().split())
tmts = []
result = -1

for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    tmts.append(temp)

is_already_done = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tmts[i][j][k] == 1:
                q.append([i, j, k])
            if tmts[i][j][k] == 0:
                is_already_done = False

bfs()

# bfs 종료 후 토마토가 다 익지 않은 경우
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tmts[i][j][k] == 0:
                print(-1)
                sys.exit(0)

# 입력받은 토마토가 이미 다 익은 경우
if is_already_done:
    print(0)
# 그 외의 경우
else:
    print(result - 1)