## time - O(n + klogn), space - O(n)
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_cnts = Counter(words)
        hq = [(-c, w) for w, c in words_cnts.items()]
        heapq.heapify(hq)

        res = []
        for i in range(k):
            _, w = heapq.heappop(hq)
            res.append(w)
        return res