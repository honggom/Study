# 실버 3
# 14425. 문자열 집합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set([input().rstrip() for _ in range(n)])

count = 0
for _ in range(m):
    if input().rstrip() in s:
        count += 1

print(count)