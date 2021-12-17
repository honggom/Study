# 실버 3
# 20291. 파일 정리

import sys
import collections
input = sys.stdin.readline

n = int(input())
exts = collections.defaultdict(int)

for _ in range(n):
    ext = input().rstrip().split('.')[1]
    exts[ext] += 1

[print(e, exts[e]) for e in sorted(exts)]