import sys
arr = []
for _ in range(int(sys.stdin.readline())):
    arr.append(list(map(int, sys.stdin.readline().split())))

for val in sorted(arr, key=lambda x : (x[1], x[0])):
    print(val[0], val[1])
