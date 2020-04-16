class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.count = n

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        rootI = self.find(i)
        rootJ = self.find(j)
        if rootI != rootJ:
            if self.size[rootI] < self.size[rootJ]:
                rootI, rootJ = rootJ, rootI
            self.parent[rootJ] = rootI
            self.size[rootI] += self.size[rootI]
            self.count -= 1


## time - O(N**2*W), space - O(N)
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        n = len(A)
        if n <= 1:
            return n
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if uf.find(i) == uf.find(j):
                    continue
                if self.helper(A[i], A[j]):
                    uf.union(i, j)
        return uf.count

    def helper(self, w1, w2):
        cnt = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
            if cnt > 2:
                return False
        return True