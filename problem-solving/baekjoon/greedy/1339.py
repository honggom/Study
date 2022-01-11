# 골드 4
# 1339. 단어 수학

import sys
input = sys.stdin.readline

dic = {chr(i): 0 for i in range(65, 91)}
temp = []
count = 0

for _ in range(int(input())):
    s = list(input().rstrip())

    for i in range(len(s)):
        num = 10 ** (len(s) - i - 1)
        dic[s[i]] += num

for k in dic.items():
    if k[1] > 0:
        temp.append(k[1])

num = 9
for t in sorted(temp, reverse=True):
    count += t * num
    num -= 1

print(count)