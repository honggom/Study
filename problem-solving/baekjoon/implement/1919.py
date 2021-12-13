# 브론즈 2
# 1919. 애너그램 만들기

s1 = list(input())
s2 = list(input())
intersection = []
count = 0

for s in s1:
    if s in s2:
        intersection.append(s)
        s2[s2.index(s)] = '*'

count += len(s1) - len(intersection)
count += len(s2) - len(intersection)

print(count)