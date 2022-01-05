# 실버 3
# 20920. 영단어 암기는 괴로워

import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []

for _ in range(n):
    c = input().rstrip()
    if len(c) >= m:
        s.append(c)

counted = collections.Counter(s)
seted = list(set(s))

[print(r) for r in sorted(seted, key=lambda x: (-counted[x], -len(x), x))]
