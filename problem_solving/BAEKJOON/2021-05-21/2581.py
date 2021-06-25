# 소수 구하기 2
m = int(input())
n = int(input())
tmp = []
result = []
for i in range(m, n+1):
    if i != 1:
        for j in range(i):
            if i / (j+1) == int(i / (j+1)):
                tmp.append(i / (j+1))
        if len(tmp) == 2:
            result.append(i)
        tmp = []
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])
