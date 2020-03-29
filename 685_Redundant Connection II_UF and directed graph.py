class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n + 1)]

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            root[rootY] = rootX
            return True

        pointed_to = {}
        can1, can2 = [], []
        for start, end in edges:
            if end in pointed_to:
                can1, can2 = pointed_to[end], [start, end]
                break
            pointed_to[end] = [start, end]

        for start, end in edges:
            if [start, end] == can2:
                continue
            if not union(start, end):
                if can1:
                    return can1
                else:
                    return [start, end]
        return can2