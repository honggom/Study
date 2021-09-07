from collections import deque
import sys

a, b = map(int, input().split())
q = deque()
q.append([a, 0])

while q:
    num, depth = q.popleft()
    if num == b:
        print(depth + 1)
        sys.exit(0)
    if b >= num * 2:
        q.append([num * 2, depth + 1])
    if b >= int(str(num) + str(1)):
        q.append([int(str(num) + str(1)), depth + 1])

print(-1)