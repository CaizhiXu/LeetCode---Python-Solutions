## dfs, space - O(N), time - O(N^^2)
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(start, end):
            visited.add(start)
            if start == end:
                return True
            for nei in graph[start]:
                if nei not in visited and dfs(nei, end):
                    return True
            return False

        for start, end in edges:
            visited = set()
            if start in graph and end in graph:
                if dfs(start, end):
                    return [start, end]
            graph[start].append(end)
            graph[end].append(start)


## UF

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num = len(edges)
        result = []
        comp = [i for i in range(num + 1)]

        def root(x):
            while comp[x] != x:
                comp[x] = comp[comp[x]]
                x = comp[x]
            return x

        def union(a, b):
            comp[root(a)] = comp[root(b)]

        for edge in edges:
            if root(edge[0]) != root(edge[1]):
                union(edge[0], edge[1])
            else:
                result.append([edge[0], edge[1]])

        return result[-1]