def bfs(graph, start):
    visited, need_visit = [], []

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            if node in graph:
                need_visit.extend(graph[node])

    return visited

# graph는 Key, Value형태의 dict로 돼 있어야 됨

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'G', 'H', 'I'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C'],
    'I': ['C', 'J'],
    'J': ['I']
}

print(bfs(graph, 'A'))
