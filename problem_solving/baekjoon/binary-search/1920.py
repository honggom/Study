from sys import stdin
stdin.readline()
nums = sorted(list(map(int, stdin.readline().split())))
stdin.readline()
find_nums = list(map(int, stdin.readline().split()))

for fn in find_nums:
    if fn in nums:
        print(1)
    else:
        print(0)


