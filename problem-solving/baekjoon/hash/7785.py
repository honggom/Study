# 실버 5
# 7785. 회사에 있는 사람
import sys
input = sys.stdin.readline

dic = {}

for _ in range(int(input())):
    s = input().split()
    dic[s[0]] = s[1]

for k in sorted(dic.keys(), reverse=True):
    if dic[k] == 'enter':
        print(k)