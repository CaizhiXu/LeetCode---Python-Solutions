from collections import deque
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.lists = deque()
        for v in [v1, v2]:
            if len(v):
                self.lists.append((len(v), iter(v)))

    def next(self) -> int:
        if not self.hasNext:
            return
        length, ite = self.lists.popleft()
        res = next(ite)
        if length-1>0:
            self.lists.append((length-1, ite))
        return res

    def hasNext(self) -> bool:
        return len(self.lists) != 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())