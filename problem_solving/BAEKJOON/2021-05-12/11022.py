import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
    data = list(map(int, sys.stdin.readline().split(' ')))
    print("Case #%d: %d + %d = %d" % (i, data[0], data[1], (data[0]+data[1])))
