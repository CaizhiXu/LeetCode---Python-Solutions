from collections import deque, defaultdict


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = deque()
        self.count = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.time or self.time[-1] != timestamp:
            self.time.append(timestamp)
        self.count[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.time and timestamp - self.time[0] >= 300:
            time = self.time.popleft()
            del self.count[time]
        return sum(self.count.values())

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)