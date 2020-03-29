## time - klogn2, space - n2
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        hq = []
        for i in range(len(nums2)):
            hq.append((nums1[0] + nums2[i], 0, i))
        heapq.heapify(hq)

        res = []
        for i in range(k):
            if not hq:
                break  # k too large
            _, idx1, idx2 = heapq.heappop(hq)
            res.append([nums1[idx1], nums2[idx2]])
            if idx1 + 1 < len(nums1):
                heapq.heappush(hq, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
        return res