# 실버 4
# 2217. 로프

import sys
input = sys.stdin.readline
ropes = [int(input())for _ in range(int(input()))]

count = 1
result = 0

for rope in sorted(ropes, reverse=True):
    result = max(result, count * rope)
    count += 1

print(result)