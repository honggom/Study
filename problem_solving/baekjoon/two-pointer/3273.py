from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
x = int(stdin.readline())
count = 0

nums.sort()
left, right = 0, n-1

while left < right:
    sum_num = nums[left] + nums[right]
    if sum_num == x:
        left += 1
        right -= 1
        count += 1
    elif sum_num > x:
        right -= 1
    else:
        left += 1
print(count)

