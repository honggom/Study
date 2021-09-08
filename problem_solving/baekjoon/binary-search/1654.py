import sys

k, n = map(int, input().split())
lans = [int(sys.stdin.readline()) for _ in range(k)]
left, right = 1, max(lans)

while left <= right:
    mid = (left + right) // 2
    count = 0

    for lan in lans:
        count += lan // mid
    if count >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)