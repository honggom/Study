import sys
import collections
input = sys.stdin.readline

n = int(input())
nums = collections.Counter(list(map(int, input().split())))
m = int(input())
target = list(map(int, input().split()))

for t in target:
    try:
        print(nums[t], end=" ")
    except:
        print(0, end=" ")