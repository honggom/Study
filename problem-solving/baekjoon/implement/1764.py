# 실버 4
# 1764. 듣보잡

import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
dic = defaultdict(int)

for _ in range(n + m):
    name = input().strip()
    dic[name] += 1

result = []

for key in dic.keys():
    if dic[key] == 2:
        result.append(key)

print(len(result))
[print(r) for r in sorted(result)]