# 위상정렬
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
inDegree = [0 for i in range(32001)]
graph = [[] for i in range(32001)]
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    student = q.popleft()

    for i in graph[student]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)
    print(student, end=" ")