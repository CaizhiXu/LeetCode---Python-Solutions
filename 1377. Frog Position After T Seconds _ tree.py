## time, space - O(n)
from collections import defaultdict, deque
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree = defaultdict(list)
        visited = set()
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)
        dq = deque([(1, 0, 1)]) ## node, time, probability
        visited.add(1)
        while dq:
            node, time, p = dq.popleft()
            num = 0
            if time == t and node == target:
                return p
            if time > t:
                return 0
            for nei in tree[node]:
                if nei not in visited:
                    num += 1
            if num == 0:
                if node == target:
                    return p
            for nei in tree[node]:
                if nei not in visited:
                    visited.add(nei)
                    dq.append((nei, time+1, p/num))
        return 0