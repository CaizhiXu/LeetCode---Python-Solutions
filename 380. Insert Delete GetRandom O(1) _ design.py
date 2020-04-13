import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dct = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dct:
            return False
        self.list.append(val)
        self.length += 1
        self.dct[val] = self.length - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dct:
            return False
        idx = self.dct[val]
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
        self.dct[self.list[idx]] = idx
        self.list.pop()
        self.length -= 1
        del self.dct[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.list:
            return None
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()