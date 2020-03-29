## time, space - O(N)
from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flowers = [0] * (N + 1)
        graph = defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)

        for garden in range(1, N + 1):
            flowers[garden] = ({1, 2, 3, 4} - set([flowers[nei] for nei in graph[garden]])).pop()

        return flowers[1:]