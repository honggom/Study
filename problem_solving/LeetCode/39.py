class Solution:
    def combinationSum(self, candidates, target):

        results = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                results.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])

        return results

'''
csum : candidates sum
index가 항상 자기부터 시작한다는 것이 포인트 
'''

s = Solution()
s.combinationSum([2,3,6,7], 7)