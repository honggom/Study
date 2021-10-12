# 프림 알고리즘
import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
visited = [False] * (v + 1)
edges = [[] for _ in range(v + 1)]
heap = [[0, 1]]

for _ in range(e):
    s, e, w = map(int, input().split())
    edges[s].append([w, e])
    edges[e].append([w, s])

result = 0
escape_count = 0

while heap:
    if escape_count == v:
        break

    weight, now = heapq.heappop(heap)

    if not visited[now]:
        visited[now] = True
        result += weight
        escape_count += 1
        for i in edges[now]:
            heapq.heappush(heap, i)

print(result)