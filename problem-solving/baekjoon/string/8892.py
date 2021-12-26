# 실버 5
# 8892. 팰린드롬

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    strs = []
    pal = []

    for _ in range(int(input())):
        strs.append(input().rstrip())

    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            s1, s2 = strs[i] + strs[j], strs[j] + strs[i]

            if s1 == s1[::-1]:
                pal.append(s1)
            if s2 == s2[::-1]:
                pal.append(s2)

    if pal:
        print(pal[0])
    else:
        print(0)