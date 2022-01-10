# 실버 1
# 1946. 신입 사원

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    nums = [list(map(int, input().split())) for _ in range(int(input()))]
    count = 0
    pivot = None
    for s in sorted(nums, key=lambda x: x[0]):
        if not pivot:
            pivot = s[1]
        else:
            if pivot > s[1]:
                count += 1
                pivot = s[1]
    print(count + 1)