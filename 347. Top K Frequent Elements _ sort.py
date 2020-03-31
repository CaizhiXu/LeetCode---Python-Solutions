## time - O(n + klogn), space - O(n)
collections
import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnts = Counter(nums)
        hq = []
        for num, cnt in num_cnts.items():
            hq.append((-cnt, num))
        heapq.heapify(hq)

        res = []
        for i in range(k):
            _, num = heapq.heappop(hq)
            res.append(num)
        return res