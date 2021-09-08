import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for i in range(n)]
houses = []
house = 0

def dfs(i, j):
    global house

    if i < 0 or j < 0 or j >= n or i >= n or graph[i][j] == 0:
        return
    graph[i][j] = 0
    house += 1

    # 동서남북 탐색
    dfs(i + 1, j)
    dfs(i, j + 1)
    dfs(i - 1, j)
    dfs(i, j - 1)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            houses.append(house)
            house = 0

print(len(houses))
for i in sorted(houses):
    print(i)
