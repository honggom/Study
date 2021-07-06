'''
10
0
1 0
1
0 1
2
1 1
3
1 2
4
2 3
5
3 5
6
5 8
7
8 13
8
13 21
9
21 34
'''
# 시간초과
'''
def zero_func():
    global zero
    zero += 1
    return zero
    
def one_func():
    global one
    one += 1
    return one

def fibo(num):
    if num == 0:
        return zero_func()
    elif num == 1:
        return one_func()
    else:
        return fibo(num - 1) + fibo(num - 2)

from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    zero = 0
    one = 0
    fibo(int(stdin.readline()))
    print(zero, one)
'''

# 정답풀이
t = int(input())
for i in range(t):
    n = int(input())
    zero, one = 1, 0
    for _ in range(n):
        one, zero = one + zero, one
    print(zero, one)