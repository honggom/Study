input()
nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    start_num = nums[0]
    target_num = nums[i]
    stay = True
    while stay and target_num != 1:
        for j in range(2, target_num + 1):
            if target_num / j == int(target_num / j) and start_num / j == int(start_num / j):
                start_num, target_num = int(start_num / j), int(target_num / j)
                break
            elif target_num == j:
                stay = False

    print(f'{start_num}/{target_num}')





