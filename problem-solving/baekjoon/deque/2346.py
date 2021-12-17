# 실버 3
# 2346. 풍선 터뜨리기

import sys
import collections
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
q = collections.deque([i for i in range(1, n + 1)])
result = []
dic = {q[i]: nums[i] for i in range(n)}

for _ in range(len(nums)):
    poped = q.popleft()
    result.append(str(poped))

    r = dic[poped]
    if r > 0:
        q.rotate(-(r - 1))
    elif r < 0:
        q.rotate(-r)

print(" ".join(result))