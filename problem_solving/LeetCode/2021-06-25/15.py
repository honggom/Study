'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

def sum(nums:list):
    result = []
    nums.sort()
    for i in range(len(nums)-1):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            num = nums[i] + nums[left] + nums[right]
            if num > 0:
                right -= 1
            elif num < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
    return result

#l = [-1, 0, 1, 2, -1, -4]
l = [-2,0,1,1,2]
print(sum(l))
