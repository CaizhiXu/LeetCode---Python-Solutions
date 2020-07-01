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


## time - O(n), space - O(n)
import heapq
import random


class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        brutal force: O(nlogn), O(n)
        quickSelect: O(n), O(1)
        points[:K]
        """
        if not points or K >= len(points):
            return points

        l, r = 0, len(points) - 1
        while l < r:
            pos = self.partition(points, l, r)
            if pos + 1 == K:
                break
            elif pos + 1 < K:
                l = pos + 1
            else:
                r = pos - 1
        return points[:K]

    def partition(self, points, l, r):
        idx = random.randint(l, r)
        points[idx], points[r] = points[r], points[idx]
        i = l
        while i < r:
            if self.distance(points[i]) < self.distance(points[r]):
                points[i], points[l] = points[l], points[i]
                l += 1
            i += 1
        points[r], points[l] = points[l], points[r]
        return l

    def distance(self, pos):
        x, y = pos
        return x ** 2 + y ** 2