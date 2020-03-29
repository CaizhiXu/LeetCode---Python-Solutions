## time, space - O(N!)
from collections import defaultdict


class Solution:
    def countArrangement(self, N: int) -> int:
        graph = defaultdict(set)
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                if j % i == 0:
                    graph[i].add(j)
                    graph[j].add(i)
        arr = [i for i in range(1, N + 1)]
        return self.dfs(1, N, arr, graph)

    def dfs(self, i, N, arr, graph):
        if not arr:
            return 1
        cnt = 0
        for j in range(len(arr)):
            if arr[j] in graph[i]:
                cnt += self.dfs(i + 1, N, arr[:j] + arr[j + 1:], graph)
        return cnt