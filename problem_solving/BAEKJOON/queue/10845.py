from sys import stdin
from collections import deque
n = int(stdin.readline())
q = deque()
for _ in range(n):
    cmd = stdin.readline().split()

    if len(cmd) == 2:
        q.append(cmd[1])
    elif cmd[0] == 'front':
        print(q[0] if len(q) != 0 else -1)
    elif cmd[0] == 'back':
        print(q[len(q) - 1] if len(q) != 0 else -1)
    elif cmd[0] == 'empty':
        print(1 if len(q) == 0 else 0)
    elif cmd[0] == 'size':
        print(len(q))
    else:
        print(q.popleft() if len(q) != 0 else -1)