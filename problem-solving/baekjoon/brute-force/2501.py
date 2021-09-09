n, k = map(int, input().split())
nums = []

for i in range(n, 0, -1):
    if n % i == 0:
        nums.append(i)
try:
    print(nums[-k])
except:
    print(0)