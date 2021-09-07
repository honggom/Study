import sys
import collections
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = collections.defaultdict(list)
friends = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

if not graph[1]:
    print(0)
else:
    for i in graph[1]:
        friends.append(i)
        if i in graph:
            for j in graph[i]:
                friends.append(j)

    friends = set(friends)

    print(len(friends) - 1)


