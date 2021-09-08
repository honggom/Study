from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
dq = deque([i+1 for i in range(n)])
result = []

while dq:
    dq.rotate(-(k-1))
    result.append(str(dq.popleft()))

sys.stdout.write("<"+", ".join(result)+">")
