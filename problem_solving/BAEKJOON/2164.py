from collections import deque
dq = deque([item for item in range(1, int(input()) + 1)])

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())
