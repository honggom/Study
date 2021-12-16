# 실버 3
# 5397. 키로거

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cmd = list(input().rstrip())
    left = []
    right = []

    for c in cmd:
        if c == '<':
            if left:
                right.append(left.pop())
        elif c == '>':
            if right:
                left.append(right.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)

    print("".join(left) + "".join(reversed(right)))



