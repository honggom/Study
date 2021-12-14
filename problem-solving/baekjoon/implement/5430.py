# 골드 5
# 5430. AC

from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())

for i in range(t):
    p = input().rstrip()
    n = int(input())
    q = deque(input().rstrip()[1:-1].split(","))

    left = True
    isEmpty = False

    if n == 0:
        q = []

    for j in p:
        if j == 'R':
            left = not left
        elif j == 'D':
            if len(q) < 1:
                isEmpty = True
                print("error")
                break
            else:
                if left:
                    q.popleft()
                else:
                    q.pop()
    if not isEmpty:
        if left:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")