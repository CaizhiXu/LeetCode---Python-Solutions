## time - O(E+V+ElogE), space - O(V+E), Prim's algo
import heapq
from collections import defaultdict


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        hq = [(0, 0)]
        graph = defaultdict(list)

        for a, b, cost in pipes:
            graph[a].append((b, cost))
            graph[b].append((a, cost))
        for i, cost in enumerate(wells, 1):
            graph[0].append((i, cost))
            graph[i].append((0, cost))

        res, num = 0, -1
        visited = set()
        while hq:
            cost, house = heapq.heappop(hq)
            if house in visited:
                continue
            visited.add(house)
            res += cost
            num += 1
            if num == n:
                return res
            for nei, newCost in graph[house]:
                if nei not in visited:
                    heapq.heappush(hq, (newCost, nei))


## based on UF
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        n += 1
        parent = [i for i in range(0, n)]

        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]

        def union(house1, house2, cost):
            root1 = find(house1)
            root2 = find(house2)
            if root1 != root2:
                parent[root2] = root1
                return cost
            return 0

        edges = [(wells[i - 1], 0, i) for i in range(1, n)]
        for house1, house2, cost in pipes:
            edges.append((cost, house1, house2))
        edges.sort()

        res = 0
        for cost, house1, house2 in edges:
            res += union(house1, house2, cost)

        return res