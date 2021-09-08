import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(x):
    global cycle
    visited[x] = True
    temp_cycle.append(x)
    num = arr[x]

    if visited[num]:
        if num in temp_cycle:
            cycle += temp_cycle[temp_cycle.index(num):]
        return
    else:
        dfs(num)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    cycle = []

    for i in range(1, n + 1):
        if not visited[i]:
            temp_cycle = []
            dfs(i)

    print(n - len(cycle))