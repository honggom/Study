graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
import heapq

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    q = []
    heapq.heappush(q, [distances[start], start])

    while q:
        cur_distance, cur_node = heapq.heappop(q)

        if distances[cur_node] < cur_distance:
            continue

        for adjacent, weight in graph[cur_node].items():
            distance = cur_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(q, [distance, adjacent])

    return distances


print(dijkstra(graph, 'A'))