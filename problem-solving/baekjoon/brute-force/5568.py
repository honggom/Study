# 실버 5
# 5568. 카드 놓기

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
nums = [int(input()) for _ in range(n)]
result = set()
temp = []
visited = [False] * n

def dfs():
    if len(temp) == k:
        result.add("".join(map(str, temp)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp.append(nums[i])
            dfs()
            temp.pop()
            visited[i] = False

dfs()
print(len(result))