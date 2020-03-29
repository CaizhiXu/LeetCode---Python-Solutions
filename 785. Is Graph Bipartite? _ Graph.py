# time - O(V+E), space - O(V)
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for node in range(n):
            if colors[node] == 0 and graph[node]:
                if not self.bfs(node, graph, colors):
                    return False
        return True

    def bfs(self, node, graph, colors):
        dq = deque([node])
        # dq.append(node)
        colors[node] = 1  # part A
        while dq:
            node = dq.pop()
            for nei in graph[node]:
                if colors[nei] == 0:
                    colors[nei] = 3 - colors[node]
                    dq.appendleft(nei)
                elif colors[nei] == colors[node]:
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not self.dfs(node, graph, color):
                    return False
        return True

    def dfs(self, node, graph, color):
        for nei in graph[node]:
            if nei not in color:
                color[nei] = 1 - color[node]
                if not self.dfs(nei, graph, color):
                    return False
            else:
                if color[nei] == color[node]:
                    return False
        return True