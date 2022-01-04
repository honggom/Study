# 실버 3
# 17204. 죽음의 게임

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dic = {i: int(input())for i in range(n)}

cur = 0

for i in range(n):
    if cur == k:
        print(i)
        sys.exit(0)
    cur = dic[cur]
print(-1)