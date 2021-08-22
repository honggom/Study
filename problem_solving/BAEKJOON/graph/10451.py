import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)

for _ in range(int(input())):
    n = int(input())
    nodes = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        graph[i].append(nodes[i - 1])
        graph[nodes[i - 1]].append(i)

    count = 0
    for i in range(1, n+1):
        if not visited[i]:
            count += 1
            dfs(i, visited)

    print(count)