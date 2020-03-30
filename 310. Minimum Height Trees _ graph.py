## time, space - O(E+V)
from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegrees[a] += 1
            indegrees[b] += 1

        dq = deque([i for i in indegrees if indegrees[i] == 1])
        while n > 2:
            length = len(dq)
            for i in range(length):
                leaf = dq.pop()
                n -= 1
                for nei in graph[leaf]:
                    indegrees[nei] -= 1
                    if indegrees[nei] == 1:
                        dq.appendleft(nei)
        res = list(dq)
        return res