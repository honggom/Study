import heapq
import sys
from collections import defaultdict

n, m = map(int, input().split())

graph = defaultdict(list)
distances = [sys.maxsize] * (n + 1)
start = int(input())

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

q = []

heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)

    if distances[now] < dist:
        continue

    for node in graph[now]:
        cost = dist + node[1]
        if distances[node[0]] > cost:
            distances[node[0]] = cost
            heapq.heappush(q, (cost, node[0]))

for i in range(1, n + 1):
    if i == start:
        print(0)
    elif distances[i] == sys.maxsize:
        print("INF")
    else:
        print(distances[i])