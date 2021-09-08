results = []

n = 4
k = 2
tmp = []

def dfs(nums):
    if len(nums) == k:
        results.append(nums)
        return

    for num in range(1, n + 1):
        nums = [num]
        if num not in nums:
            tmp
            dfs(nums)

