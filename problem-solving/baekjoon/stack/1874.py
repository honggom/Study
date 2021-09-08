from collections import deque

n = int(input())
given_nums, stack, result = deque([int(input()) for _ in range(n)]), deque(), deque()

for i in range(n):
    stack.appendleft(i+1)
    result.append("+")
    while len(given_nums) > 0 and len(stack) > 0 and given_nums[0] == stack[0]:
        given_nums.popleft()
        stack.popleft()
        result.append("-")

if len(stack) > 0:
    print("NO")
else:
    [print(rtn) for rtn in result]


