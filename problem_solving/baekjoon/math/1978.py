# 소수 구하기 1
int(input())
n = list(map(int, input().split()))
count = 0
arr = []
for i in n:
    if i != 1:
        for j in range(i):
            if i / (j+1) == int(i / (j+1)):
                arr.append(i / (j+1))
        if len(arr) == 2:
            count += 1
            #print("%d는 소수임!" % (i))
        arr = []
print(count)
