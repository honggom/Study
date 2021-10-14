from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
counted = defaultdict(int)
q = deque()
q.append([n, 0])

while q:
    cur, count = q.popleft()
    visited[cur] = True

    if cur == k:
        counted[count] += 1
    else:
        if 0 <= cur + 1 <= 100000 and not visited[cur + 1]:
            q.append([cur + 1, count + 1])
        if 0 <= cur - 1 <= 100000 and not visited[cur - 1]:
            q.append([cur - 1, count + 1])
        if 0 <= cur * 2 <= 100000 and not visited[cur * 2]:
            q.append([cur * 2, count + 1])

for key in counted.keys():
    print(key)
    print(counted[key])
    sys.exit(0)