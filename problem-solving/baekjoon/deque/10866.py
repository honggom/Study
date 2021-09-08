from sys import stdin
from collections import deque

test_case = int(stdin.readline())
dq = deque()

for _ in range(test_case):

    cmd = stdin.readline().split()

    if len(cmd) == 2:
        if cmd[0] == 'push_front':
            dq.appendleft(int(cmd[1]))
        else:
            dq.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        print(-1 if len(dq) == 0 else dq.popleft())
    elif cmd[0] == 'pop_back':
        print(-1 if len(dq) == 0 else dq.pop())
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        print(1 if len(dq) == 0 else 0)
    elif cmd[0] == 'front':
        print(dq[0] if len(dq) != 0 else -1)
    elif cmd[0] == 'back':
        print(dq[len(dq)-1] if len(dq) != 0 else -1)
