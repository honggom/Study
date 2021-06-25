import sys

input1 = int(input())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

print("%d %d" % (arr[0], arr[input1-1]))
