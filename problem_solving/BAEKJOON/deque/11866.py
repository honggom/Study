from collections import deque
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
result = []

q.rotate(-(abs(k - 1)))
while q:
    result.append(q.popleft())
    q.rotate(-(abs(k - 1)))

print("<"+", ".join(map(str, result))+">")