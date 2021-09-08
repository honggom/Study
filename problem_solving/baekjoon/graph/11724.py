import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i, visited)

print(count)