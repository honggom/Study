import collections
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:

        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for y in graph[node]:
                if not dfs(y):
                    return False

            visited.remove(node)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True