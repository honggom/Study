n = int(input())

min_constructor = 0

for i in range(n, 0, -1):
    nums = list(map(int, list(str(i))))
    constructor = i
    for num in nums:
        constructor += num
    if constructor == n:
        min_constructor = i
print(min_constructor)


