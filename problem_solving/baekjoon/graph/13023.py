import sys
input = sys.stdin.readline

finshed = False
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start, depth):
    global finshed
    visited[start] = True

    if depth == 4:
        finshed = True
        return
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if finshed:
        break

print(1 if finshed else 0)















