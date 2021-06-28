from collections import deque
from sys import stdin

for i in range(int(stdin.readline())):
    dq = deque(stdin.readline().split())
    s = ''
    while len(dq) > 0:
        s += dq.pop() + ' '
    print(f'Case #{i+1}: '+s)
