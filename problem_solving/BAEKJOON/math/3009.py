# 네 번째 점
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
xList = [a, c, e]
yList = [b, d, f]
result = []
for i in xList:
    if xList.count(i) == 1:
        result.append(i)
for j in yList:
    if yList.count(j) == 1:
        result.append(j)
print(result[0], result[1])
