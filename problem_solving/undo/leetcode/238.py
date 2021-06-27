'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
# 첫 풀이

nums = [1,2,3,4]
result = []
tmp = 1
for i in range(len(nums)):
    for j in range(len(nums)):
        if j != i:
            tmp = nums[j] * tmp
    result.append(tmp)
    tmp = 1
print(result)
'''
nums = [1, 2, 3, 4]
result = []
tmp_num = 1
for val in nums:
    nums.remove(val)
    for val2 in nums:
        tmp_num = tmp_num * val2
    print(nums)
    result.append(tmp_num)
    tmp_num = 1
    nums.append(val)
print(result)

