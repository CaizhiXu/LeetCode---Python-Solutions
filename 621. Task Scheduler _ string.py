from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        [ABC], n+1
        [ABC],
        [AB],
        max Count: maxC, k
        (maxC-1)*(n+1) + k
        k*maxC + max(tot - k*maxC, (maxC-1)*(n+1-k))

        """
        cnts = Counter(tasks)
        maxC = max(cnts.values())
        k = 0
        for key, val in cnts.items():
            if val == maxC:
                k += 1
        tot = len(tasks)

        to_fill = (maxC - 1) * (n + 1 - k)
        available = tot - k * maxC
        res = k * maxC + max(to_fill, available)
        return res