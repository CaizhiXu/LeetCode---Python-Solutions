## time - nk(lognk), space - O(nk)
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = {i: [] for i in range(n)}
        for s, t, p in flights:
            graph[s].append((t, p))

        cost = {(0, src): 0}
        hq = [(0, src, 0)]  # cost, city, stop
        while hq:
            price, city, stop = heapq.heappop(hq)
            if city == dst:
                return price
            if stop == K + 1:
                continue
            for nei, p in graph[city]:
                if price + p < cost.get((stop + 1, nei), float('inf')):
                    cost[(stop + 1, nei)] = price + p
                    heapq.heappush(hq, (price + p, nei, stop + 1))
        return -1