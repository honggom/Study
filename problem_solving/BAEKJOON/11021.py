import sys
T = int(input())
for i in range(1, T+1):
    data = list(map(int, sys.stdin.readline().split(' ')))
    print("Case #"+str(i)+": "+str(data[0]+data[1]))
