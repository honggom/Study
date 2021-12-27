# 브론즈 1
# 1357. 뒤집힌 덧셈

import sys
input = sys.stdin.readline

a, b = input().split()

def rev(n):
    return int(''.join((str(n)[::-1])))

print(rev(rev(a) + rev(b)))