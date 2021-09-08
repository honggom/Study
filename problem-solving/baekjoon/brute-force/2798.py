n, m = map(int, input().split())
nums = list(map(int, input().split()))


def balck_jack(nums, m):
    answer = 0
    for i in nums:
        copy_list = nums[:]
        copy_list.remove(i)
        nums2 = copy_list
        for j in nums2:
            copy_list.remove(j)
            nums3 = copy_list
            for k in nums3:
                if i+j+k == m:
                    return m
                else:
                    if answer < i+j+k <= m:
                        answer = i+j+k
    return answer


print(balck_jack(nums, m))