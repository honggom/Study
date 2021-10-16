from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
path = defaultdict(list)

q = deque()
q.append([n, 0])

while q:
    cur, count = q.popleft()
    visited[cur] = True

    path[count].append(cur)

    if cur == k:
        print(count)
        break

    if 0 <= cur + 1 <= 100000 and not visited[cur + 1]:
        q.append([cur + 1, count + 1])
    if 0 <= cur - 1 <= 100000 and not visited[cur - 1]:
        q.append([cur - 1, count + 1])
    if 0 <= cur * 2 <= 100000 and not visited[cur * 2]:
        q.append([cur * 2, count + 1])

result = []
result.append(k)
temp = k

for i in range(count - 1, 0, -1):
    if temp / 2 in path[i]:
        result.append(int(temp / 2))
        temp = int(temp / 2)
    elif temp - 1 in path[i]:
        result.append(temp - 1)
        temp = temp - 1
    elif temp + 1 in path[i]:
        result.append(temp + 1)
        temp = temp + 1

result.append(n)

if n == k:
    print(k)
else:
    print(" ".join(map(str, result[::-1])))