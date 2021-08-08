from sys import stdin


def dfs(graph, start):
    visited, need_visit = [], []
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                need_visit.extend(sorted(graph[node], reverse=True))

    return visited


def bfs(graph, start):
    visited, need_visit = [], []
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            if node in graph:
                need_visit.extend(sorted(graph[node]))

    return visited


vertex_count, edge_count, start = map(int, stdin.readline().split())
graph = dict()

for _ in range(edge_count):
    v1, v2 = map(int, stdin.readline().split())
    if v1 in graph:
        graph[v1].append(v2)
    else:
        graph[v1] = [v2]

    if v2 in graph:
        graph[v2].append(v1)
    else:
        graph[v2] = [v1]

print(" ".join(map(str, dfs(graph, start))))
print(" ".join(map(str, bfs(graph, start))))
