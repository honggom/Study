n, m = map(int, input().split())
nums = list(map(int, input().split()))

p1, p2 = 0, 0
count = 0

while p2 < n and p1 < n:
    if sum(nums[p1:p2+1]) < m:
        p2 += 1
    elif sum(nums[p1:p2+1]) == m:
        count += 1
        if p1 < p2:
            p1 += 1
        else:
            p2 += 1
    else:
        p1 += 1

print(count)