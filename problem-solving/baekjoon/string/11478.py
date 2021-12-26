# 실버 3
# 11478. 서로 다른 부분 문자열의 개수

import sys
input = sys.stdin.readline

s = input().rstrip()
result = set()

for i in range(1, len(s) + 1):
    for j in range(len(s) + 1 - i):
        result.add(s[j:j + i])

print(len(result))