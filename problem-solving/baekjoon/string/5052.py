# 골드 4
# 5052. 전화번호 목록

from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    nums.sort()

    flag = False
    for i in range(1, n):
        if nums[i].startswith(nums[i - 1]):
            flag = True
            break
    if flag:
        print("NO")
    else:
        print("YES")
