# 실버 3
# 1431. 시리얼 번호

import sys
input = sys.stdin.readline

s = [input().rstrip() for _ in range(int(input()))]

def sort2(x):
    n = 0
    for c in list(x):
        if c.isdigit():
            n += int(c)
    return n

[print(c) for c in sorted(s, key=lambda x: (len(x), sort2(x), x))]