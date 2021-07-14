n = int(input())

min_constructor = 0

for cur_num in range(n, 0, -1):
    constructor = cur_num
    nums = list(map(int, list(str(cur_num))))
    for num in nums:
        constructor += num
    if constructor == n:
        min_constructor = cur_num
print(min_constructor)


