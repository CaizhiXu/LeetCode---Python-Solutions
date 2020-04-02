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



## Solution2, more object-oriented
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self.list.delete(self.cache[key])
        self.list.append(self.cache[key])
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.list.delete(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = ListNode(key, value)
        self.list.append(self.cache[key])

        if len(self.cache) > self.capacity:
            oldestNode = self.list.head.next
            del self.cache[oldestNode.key]
            self.list.delete(oldestNode)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)