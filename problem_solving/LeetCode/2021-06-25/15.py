'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

def sum(nums:list):
    result = {}
    nums.sort()
    for i in range(len(nums)-1):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            num = nums[i] + nums[left] + nums[right]
            if num == 0:
                result[str(nums[i])+str(nums[left])+str(nums[right])] = [nums[i], nums[left], nums[right]]
                break
            elif num > 0:
                right -= 1
            else:
                left += 1
    return list(result.values())

#l = [-1, 0, 1, 2, -1, -4]
l = [-2,0,1,1,2]
print(sum(l))
