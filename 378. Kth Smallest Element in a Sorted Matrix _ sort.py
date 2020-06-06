# time log(max-min)*n, space - O(1)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            cnt = self.helper(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left

    def helper(self, matrix, num):
        ## return # of elements no bigger than num
        j = len(matrix[0]) - 1
        cnt = 0
        for i in range(len(matrix)):
            while j >= 0 and matrix[i][j] > num:
                j -= 1
            if j == -1:
                break
            cnt += j + 1
        return cnt


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