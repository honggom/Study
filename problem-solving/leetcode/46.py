class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        tmp = []

        def recursive(nums):
            if len(nums) == 0:
                result.append(tmp[:])
                return

            for num in nums:
                next = nums[:]
                next.remove(num)

                tmp.append(num)
                recursive(next)
                tmp.pop()

            return result

        return recursive(nums)