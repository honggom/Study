from sys import stdin
nums = [0] * 10000
for _ in range(int(stdin.readline())):
    nums[int(stdin.readline())-1] += 1
for i in range(10000):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i+1)

