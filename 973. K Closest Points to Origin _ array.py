## time - O(n), space - O(n)
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            d = (x ** 2 + y ** 2) ** 0.5
            dist.append((d, x, y))

        self.quickSelect(dist, K)
        res = []
        for i in range(K):
            _, x, y = dist[i]
            res.append([x, y])
        return res

    def quickSelect(self, arr, K):
        left, right = 0, len(arr) - 1
        while left < right:
            l, r = left, right
            mid = l + (r - l) // 2
            arr[mid], arr[r] = arr[r], arr[mid]
            low = l
            while l < r:
                if arr[l] < arr[r]:
                    arr[l], arr[low] = arr[low], arr[l]
                    low += 1
                l += 1
            arr[low], arr[r] = arr[r], arr[low]
            if low + 1 < K:
                left = low + 1
            elif low + 1 > K:
                right = low - 1
            else:
                return