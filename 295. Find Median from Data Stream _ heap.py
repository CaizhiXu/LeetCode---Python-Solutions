## time - O(logn) + O(1), space - O(n)
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large, self.small = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        minInLarge = heapq.heappop(self.large)
        heapq.heappush(self.small, -minInLarge)

        if len(self.large) < len(self.small):
            temp = heapq.heappop(self.small)
            heapq.heappush(self.large, -temp)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()