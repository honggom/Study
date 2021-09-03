import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i):
    visited[i] = True

    for node in graph[i]:
        if not visited[node]:
            result.append(node)
            dfs(node)

dfs(1)
print(len(result))