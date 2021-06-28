import sys
c = int(input())
total = []
for _ in range(c):
    data = list(map(int, sys.stdin.readline().split()))
    personNum = data[0]
    avg = 0
    for i in range(personNum):
        avg += data[i+1]
    avg = avg / personNum
    overNumCnt = 0
    for j in range(personNum):
        if data[j+1] > avg:
            overNumCnt += 1
    total.append((overNumCnt/personNum) * 100)
for k in total:
    print("%.3f%%" % (k))
