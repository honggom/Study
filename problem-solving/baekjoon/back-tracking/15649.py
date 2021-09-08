n, m = map(int, input().split())
visited = []


def back_tracking(depth):
    if depth == m:
        print(' '.join(map(str, visited)))
        return
    for i in range(1, n + 1):
        if i not in visited:
            visited.append(i)
            back_tracking(depth + 1)
            visited.pop()

back_tracking(0)