n, m = map(int, input().split())
visited = []


def dfs(start):
    if len(visited) == m:
        print(' '.join(map(str, visited)))
        return

    for i in range(start, n + 1):
            visited.append(i)
            dfs(i)
            visited.pop()

dfs(1)