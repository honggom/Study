# 에라토스테네스의 체
import math


def magic(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num == 2:
            break
        elif num % i == 0:
            return False
    return True


m, n = map(int, input().split())
for j in range(m, n+1):
    if magic(j) == True:
        print(j)
