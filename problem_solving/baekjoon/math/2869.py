import sys
from math import ceil
day, night, height = map(int, sys.stdin.readline().split())
print(ceil((height - day) / (day - night)) + 1)
