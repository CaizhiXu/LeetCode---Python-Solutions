## time - O(nlogn), space - O(n)
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = []
        for q, w in zip(quality, wage):
            workers.append([w / q, q])
        workers.sort()

        hq = []
        total_q, res = 0, float('inf')
        for r, q in workers:
            heapq.heappush(hq, -q)
            total_q += q
            if len(hq) > K:
                total_q += heapq.heappop(hq)
            if len(hq) == K:
                res = min(res, r * total_q)
        return res