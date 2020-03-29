## time, space - O(E+V)
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        parent = [-1] * n
        disc, low = [0] * n, [0] * n
        res = []
        visited = set()
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        self.time = 0
        self.dfs(0, res, parent, disc, low, graph, visited)
        return res

    def dfs(self, node, res, parent, disc, low, graph, visited):
        disc[node], low[node] = self.time, self.time
        visited.add(node)
        self.time += 1
        for nei in graph[node]:
            if nei not in visited:
                parent[nei] = node
                self.dfs(nei, res, parent, disc, low, graph, visited)
                low[node] = min(low[node], low[nei])
                if low[nei] > disc[node]:
                    res.append((node, nei))
            elif nei != parent[node]:
                low[node] = min(low[node], disc[nei])