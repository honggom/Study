# 직사각형에서 탈출
import sys
x, y, w, h = map(int, sys.stdin.readline().split())

arr = [w - x,  h - y, x, y]
print(min(arr))
