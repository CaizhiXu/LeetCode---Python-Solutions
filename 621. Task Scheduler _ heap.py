## time - NlogN, space - O(N)
from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = Counter(tasks)
        hq = []
        for k, v in cnts.items():
            hq.append((-v, k))
        heapq.heapify(hq)
        num_intervals = 0

        while hq:
            i, temp = 0, []
            while i <= n:
                i += 1
                if hq:
                    c, task = heapq.heappop(hq)
                    if c + 1 != 0:
                        temp.append((c + 1, task))
                else:
                    if not temp:
                        break
                num_intervals += 1
            for item in temp:
                heapq.heappush(hq, item)
        return num_intervals


## time, space - O(n)
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = Counter(tasks)
        maxCnt = max(cnts.values())
        num_max = 0
        for val in cnts.values():
            if val == maxCnt:
                num_max += 1
        num_tasks = len(tasks)
        return max(num_tasks, (maxCnt-1)*(n+1) + num_max)