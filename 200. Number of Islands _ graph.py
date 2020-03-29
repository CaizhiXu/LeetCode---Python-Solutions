class UnionFind:
    def __init__(self):
        self.root = {}
        self.size = {}
        self.count = 0

    def add(self, a):
        if a not in self.root:
            self.root[a] = a
            self.size[a] = 1
            self.count += 1

    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.size[root_a] < self.size[root_b]:
                root_a, root_b = root_b, root_a
            self.root[root_b] = root_a
            self.size[root_a] += self.size[root_b]
            self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        uf = UnionFind()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    uf.add((i, j))
                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                            uf.add((ni, nj))
                            uf.union((i, j), (ni, nj))
        return uf.count