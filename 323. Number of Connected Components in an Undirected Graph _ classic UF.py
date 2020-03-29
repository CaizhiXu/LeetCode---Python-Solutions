class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        root = [i for i in range(n)]

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                root[rootB] = rootA

        for start, end in edges:
            union(start, end)

        return len(set([find(i) for i in range(n)]))