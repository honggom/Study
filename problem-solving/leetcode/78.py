class Solution:
    def subsets(self, nums):
        results = []

        def dfs(start, subset):
            results.append(subset)

            for i in range(start, len(nums)):
                dfs(i+1, subset + [nums[i]])

        dfs(0, [])
        return results

s = Solution()
print(s.subsets([1,2,3]))