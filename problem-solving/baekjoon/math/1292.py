a, b = map(int, input().split())
nums = [i for i in range(1, b + 1) for j in range(i)]
print(sum(nums[a - 1:b]))