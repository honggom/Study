# 정답풀이
t = int(input())
for i in range(t):
    n = int(input())
    zero, one = 1, 0
    for _ in range(n):
        one, zero = one + zero, one
    print(zero, one)