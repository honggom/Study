import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

m, n = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(n)]
temp = tomatos.copy()
count = 0

def dfs(i, j):
    if i < 0 or j < 0 or j >= m or i >= n:
        return
    if temp[i][j] == -1:
        return
    if temp[i][j] == 0:
        temp[i][j] = 1
        return

    # 동서남북 탐색
    dfs(i + 1, j)
    dfs(i, j + 1)
    dfs(i - 1, j)
    dfs(i, j - 1)

zero_count_history = 0
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 0:
            zero_count_history += 1

while True:
    zero_count = 0

    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 0:
                zero_count += 1
            if tomatos[i][j] == 1:
                dfs(i, j)

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 1:
                tomatos[i][j] = 1

    if zero_count == 0:
        print(count)
        break
    if zero_count_history == zero_count:
        print(-1)
        break

    zero_count_history = zero_count

    count += 1