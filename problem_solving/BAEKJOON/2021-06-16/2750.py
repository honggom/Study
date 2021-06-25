import sys
nums = []
for _ in range(int(sys.stdin.readline())):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in nums:
    print(i)