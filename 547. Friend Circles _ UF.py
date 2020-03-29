## union-find, time - O(N**2), space - O(N)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = {i: i for i in range(n)}
        size = {i: 1 for i in range(n)}

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    self.union(i, j, parent, size)

        return len(set([self.find(i, parent) for i in range(n)]))

    def find(self, x, parent):
        if x != parent[x]:
            parent[x] = self.find(parent[x], parent)
        return parent[x]

    def union(self, x, y, parent, size):
        rootX = self.find(x, parent)
        rootY = self.find(y, parent)
        if rootX != rootY:
            if size[rootX] < size[rootY]:
                rootX, rootY = rootY, rootX
            parent[rootY] = rootX
            size[rootX] += size[rootY]


## dfs, time, space - O(N)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        visited = set()
        res = 0

        for i in range(n):
            if i not in visited:
                res += 1
                self.dfs(i, n, M, visited)
        return res

    def dfs(self, i, n, M, visited):
        for j in range(n):
            if M[i][j] == 1 and j not in visited:
                visited.add(j)
                self.dfs(j, n, M, visited)