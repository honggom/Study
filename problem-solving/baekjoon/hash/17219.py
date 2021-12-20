# 실버 4
# 17219. 비밀번호 찾기

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = defaultdict(str)

for _ in range(n):
    name, pwd = input().split()
    dic[name] = pwd

for _ in range(m):
    print(dic[input().rstrip()])