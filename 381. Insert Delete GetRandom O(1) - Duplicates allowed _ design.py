from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.length = 0
        self.dct = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.list.append(val)
        self.length += 1
        self.dct[val].add(self.length - 1)
        return len(self.dct[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.dct or not self.dct[val]:
            return False
        idx = self.dct[val].pop()
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
        self.dct[self.list[idx]].add(idx)
        self.dct[self.list[idx]].remove(self.length - 1)
        self.list.pop()
        self.length -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()