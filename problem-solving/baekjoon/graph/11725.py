import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


q = deque()
q.append(1)
while q:
    node = q.popleft()
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            q.append(i)

for i in parent[2:]:
    print(i)