from collections import deque
from sys import stdin
n = int(stdin.readline())
q = deque()
for _ in range(n):
    cmd = stdin.readline().split()

    if len(cmd) == 2:
        q.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif cmd[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])