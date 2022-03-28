# 브론즈 1
# 2161. 카드1

from collections import deque

q = deque([i + 1 for i in range(int(input()))])
result = []

while q:
    result.append(q.popleft())
    if q:
        q.append(q.popleft())

print(*result)