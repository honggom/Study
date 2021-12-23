# 실버 4
# 1120. 문자열

import sys

a, b = input().split()
result = sys.maxsize

for i in range(len(b) - len(a) + 1):
    diff = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            diff += 1
    result = min(result, diff)

print(result)