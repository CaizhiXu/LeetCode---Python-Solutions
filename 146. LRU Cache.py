class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.next = {}
        self.prev = {}
        self.head, self.tail = 'head', 'tail'
        self.connect(self.head, self.tail)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.remove(key)
        self.append(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.append(key, value)

    def remove(self, key):
        del self.cache[key]
        prev, nxt = self.prev[key], self.next[key]
        del self.prev[key]
        del self.next[key]
        self.connect(prev, nxt)

    def append(self, key, val):
        self.cache[key] = val
        self.connect(self.prev[self.tail], key)
        self.connect(key, self.tail)
        if len(self.cache) > self.capacity:
            self.remove(self.next[self.head])

    def connect(self, a, b):
        self.next[a] = b
        self.prev[b] = a

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)