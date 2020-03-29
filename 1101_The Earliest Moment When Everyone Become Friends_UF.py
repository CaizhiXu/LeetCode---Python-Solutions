## time, space - O(N)
class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        parent = [i for i in range(N)]
        size = [1] * N
        logs.sort()

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] < size[rootY]:
                    rootX, rootY = rootY, rootX
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            if size[rootX] == N:
                return True
            else:
                return False

        for t, a, b in logs:
            if union(a, b):
                return t

        return -1