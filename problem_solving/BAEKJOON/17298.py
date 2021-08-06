n = int(input())
nums = list(map(int, input().split()))
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and nums[stack[-1]] < nums[i]: # 스택에 값이 있고, nums[스택에 마지막 인덱스] 값이 현재 num 보다 작으면
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)