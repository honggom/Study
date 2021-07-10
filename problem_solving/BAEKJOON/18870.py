from sys import stdin
stdin.readline()
nums = list(map(int, stdin.readline().split()))
base = sorted(list(set(nums)), reverse=True)
base_dict = {}
for index, num in enumerate(base):
    base_dict[num] = len(base) - index - 1
for num in nums:
    print(base_dict[num], end=" ")