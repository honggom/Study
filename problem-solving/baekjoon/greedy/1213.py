# 실버 4
# 1213. 팰린드롬 만들기

from collections import Counter

counted = sorted(Counter(list(input())).items())
temp = []
odds = []
s = ''

for c in counted:
    temp.append([c[0], int(c[1] / 2)])
    odd = int(c[1] % 2)

    if odd > 0:
        odds.append([c[0], odd])

for t in temp:
    s = s + (t[0] * t[1])

if len(odds) >= 2:
    print(f"I'm Sorry Hansoo")
elif len(odds) == 1:
    print(s + odds[0][0] + s[::-1])
else:
    print(s + s[::-1])

