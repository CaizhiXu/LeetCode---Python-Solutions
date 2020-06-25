## time - O(k + (n-k)logk), space - O(n)
import heapq


class Solution:
    def medianSlidingWindow(self, nums, k):
        hq_large, hq_small = [], []
        res = []

        for i in range(k):
            hq_large.append((nums[i], i))
        heapq.heapify(hq_large)
        for i in range(k >> 1):
            self.move(hq_large, hq_small)
        res.append(self.getMid(hq_large, hq_small, k))

        for i in range(k, len(nums)):
            num_add, num_rem = nums[i], nums[i - k]
            if num_add >= hq_large[0][0]:
                heapq.heappush(hq_large, (num_add, i))
                if num_rem <= hq_large[0][0]:
                    self.move(hq_large, hq_small)  ## size balancing, i-k th number is flagged to be removed
            else:
                heapq.heappush(hq_small, (-num_add, i))
                if num_rem >= hq_large[0][0]:
                    self.move(hq_small, hq_large)
            while hq_large and hq_large[0][1] <= i - k:
                heapq.heappop(hq_large)
            while hq_small and hq_small[0][1] <= i - k:
                heapq.heappop(hq_small)
            res.append(self.getMid(hq_large, hq_small, k))

        return res

    def move(self, hq1, hq2):
        num, idx = heapq.heappop(hq1)
        heapq.heappush(hq2, (-num, idx))

    def getMid(self, hq1, hq2, k):
        return hq1[0][0] if k % 2 == 1 else (hq1[0][0] - hq2[0][0]) / 2


arr = [1,3,-1,-3,5,3,6,7]
Solution().medianSlidingWindow(arr, 3)