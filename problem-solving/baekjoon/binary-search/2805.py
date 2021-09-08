import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)

while left <= right:
    _sum = 0
    mid = (left + right) // 2

    for t in trees:
        if t - mid > 0:
            _sum += t - mid

    if _sum >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)