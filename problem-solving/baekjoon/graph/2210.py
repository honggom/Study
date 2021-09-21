import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

mtx = [list(map(int, input().split())) for _ in range(5)]
result = set()

def dfs(i, j, ch):
    if len(ch) == 6:
        result.add(ch)
        return
    if i < 0 or j < 0 or i > 4 or j > 4:
        return
    ch += str(mtx[i][j])

    dfs(i, j + 1, ch)
    dfs(i, j - 1, ch)
    dfs(i + 1, j, ch)
    dfs(i - 1, j, ch)

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(result))