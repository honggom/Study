# 실버 1
# 2002. 추월

import sys
input = sys.stdin.readline

t = int(input())
s = ''
count = 0

for _ in range(t):
    s = s + ('*' + input().rstrip() + '*')

for _ in range(t):
    c = '*' + input().rstrip() + '*'
    if s.find(c) != 0:
        count += 1
    s = s.replace(c, '', 1)

print(count)