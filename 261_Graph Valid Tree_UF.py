class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 1
        root = [i for i in range(n)]

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return False
            root[rootB] = rootA
            return True

        for start, end in edges:
            if not union(start, end):
                return False

        return len(set([find(i) for i in range(n)])) == 1