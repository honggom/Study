from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
target_nums = deque(list(map(int, input().split())))
q = deque([i for i in range(1, n + 1)])
count = 0

while len(target_nums) != 0:
    if target_nums[0] == q[0]:
        target_nums.popleft()
        q.popleft()
    else:
        target_index = q.index(target_nums[0])
        mid = len(q) // 2

        if mid < target_index:
            q.rotate(1)
        elif mid >= target_index:
            q.rotate(-1)
        count += 1

print(count)