class Solution:
    def combine(self, n: int, k: int):

        results = []
        nums = []

        def dfs(start):
            if len(nums) == k:
                results.append(nums[:])
                return
            else:
                for i in range(start, n + 1):
                    if i not in nums:
                        nums.append(i)
                        dfs(i)
                        nums.pop()

        dfs(1)
        return results

s = Solution()
print(s.combine(4, 2))