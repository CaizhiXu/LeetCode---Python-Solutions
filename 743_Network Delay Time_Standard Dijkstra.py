## time - O(V+E), space - O(V)
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])

        hq = [[0, K]]
        t_rec = {K: 0}

        while hq:
            time, node = heapq.heappop(hq)
            for nextnode, nexttime in graph[node]:
                if nextnode not in t_rec or time + nexttime < t_rec[nextnode]:
                    t_rec[nextnode] = time + nexttime
                    heapq.heappush(hq, [t_rec[nextnode], nextnode])

        if len(t_rec) == N:
            return max(t_rec.values())
        else:
            return -1