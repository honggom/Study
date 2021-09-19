from collections import deque
import sys

s = input()
dq = deque(s)

while len(dq) > 1:
    if dq.pop() != dq.popleft():
        print(0)
        sys.exit(0)
print(1)



