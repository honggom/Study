from itertools import permutations

t = int(input())
nums = list(map(int, input().split()))
count = list(map(int, input().split()))
operators = ["pls", "min", "mul", "div"]
arr = []

for i in range(4):
    for j in range(count[i]):
        arr.append(operators[i])

result = []

for i in set(permutations(arr)):
    index = 0
    num = nums[index]

    for oprt in i:
        if oprt == "pls":
            num += nums[index + 1]
        elif oprt == "min":
            num -= nums[index + 1]
        elif oprt == "mul":
            num *= nums[index + 1]
        else:
            if num < 0:
                num = -(-num // nums[index + 1])
            else:
                num = num // nums[index + 1]

        index += 1

    result.append(num)

print(max(result))
print(min(result))