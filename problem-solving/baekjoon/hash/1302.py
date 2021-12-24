# 실버 4
# 1302. 베스트셀러

import collections
import sys
input = sys.stdin.readline

dic = collections.defaultdict(int)

for _ in range(int(input())):
    dic[input().rstrip()] += 1

print(sorted(sorted(dic.items()), key=lambda x: x[1], reverse=True)[0][0])