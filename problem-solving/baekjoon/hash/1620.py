# 실버 4
# 1620. 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(1, n + 1):
    name = input().rstrip()

    dic[name] = i
    dic[str(i)] = name

for _ in range(m):
    print(dic[input().rstrip()])