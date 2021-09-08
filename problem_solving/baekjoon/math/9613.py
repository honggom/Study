def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    n = nums.pop(0)
    gcd_sum = 0

    for i in range(n):
        for j in range(i+1, n):
            gcd_sum += gcd(nums[i], nums[j])

    print(gcd_sum)