# time log(max-min)*n*logn, space - O(1)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        while low + 1 < high:
            mid = low + (high - low) // 2
            cnt = self.count(matrix, mid)
            if cnt < k:
                low = mid
            else:
                high = mid

        cnt = self.count(matrix, low)
        if cnt >= k:
            return low
        else:
            return high

    def count(self, matrix, num):
        res = 0
        for row in matrix:
            res += bisect.bisect_right(row, num)
        return res


# time - O(n+klogn), space - O(n)
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)

        for _ in range(k):
            num, r, c = heapq.heappop(heap)
            if c + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
        return num