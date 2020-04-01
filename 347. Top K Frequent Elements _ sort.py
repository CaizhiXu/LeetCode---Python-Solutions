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


## time - O(n), space - O(n)
from collections import Counter
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnts = Counter(nums)
        frequency_map = {i + 1: [] for i in range(len(nums))}
        for num, cnt in num_cnts.items():
            frequency_map[cnt].append(num)

        res = []
        for freq in range(len(nums), 0, -1):
            res.extend(frequency_map[freq])
            if len(res) >= k:
                break
        return res[:k]