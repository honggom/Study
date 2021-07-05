n, m = map(int, input().split())
visited = []

def back_tracking(depth):
    if depth == m:
        for i in visited:
            print(i, end=' ')
        print()
        return
    for i in range(1, n + 1):
        if i not in visited:
            visited.append(i)
            back_tracking(depth + 1)
            visited.pop()

back_tracking(0)