# 실버 5
# 9237. 이장님 초대

input()
nums = sorted(list(map(int, input().split())), reverse=True)

for i in range(len(nums)):
    nums[i] = nums[i] + i + 1

print(max(nums) + 1)