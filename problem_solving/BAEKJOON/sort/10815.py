from sys import stdin
n = int(stdin.readline())
find_nums = dict()
for i in list(map(int, stdin.readline().split())):
    find_nums[i] = 1
m = int(stdin.readline())
target_nums = list(map(int, stdin.readline().split()))

for j in target_nums:
    try:
        print(find_nums[j], end=" ")
    except:
        print(0, end=" ")


