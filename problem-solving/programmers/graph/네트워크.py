def solution(n, computers):
    visited = [[False] * n for _ in range(n)]

    def dfs(i, j):
        visited[i][j], visited[j][i] = True, True

        for k in range(n):
            if not visited[j][k] and computers[j][k] == 1:
                dfs(j, k)

    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and computers[i][j] == 1:
                dfs(i, j)
                count += 1

    return count