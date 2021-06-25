import sys
N, X = map(int, sys.stdin.readline().split(' '))
A = list(map(int, sys.stdin.readline().split(' ')))
arr = ""
for i in range(N):
    if A[i] < X:
        arr += str(A[i])+" "
print(arr)
