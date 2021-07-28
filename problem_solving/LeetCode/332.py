from collections import defaultdict

tickets = [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        for from_, to in tickets:
            graph[from_].append(to)

        result = []

        def dfs(from_):
            while graph[from_]:
                dfs(graph[from_].pop(0))
            result.append(from_)

        dfs('JFK')

        return result[::-1]

s = Solution()
print(s.findItinerary(tickets))