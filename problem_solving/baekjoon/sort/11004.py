from sys import stdin

n, k = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

print(sorted(nums)[k - 1])