import sys
n = int(input())
t = 0
arr = list(map(int, sys.stdin.readline().split()))
m = max(arr)
for i in range(0, len(arr)):
    t += arr[i] / m * 100
print(t/n)
