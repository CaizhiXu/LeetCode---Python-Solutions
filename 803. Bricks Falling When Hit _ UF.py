class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        parent = {}
        size = {}

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

        for i, j in hits:
            grid[i][j] -= 1
        parent[(-1, -1)] = (-1, -1)
        size[(-1, -1)] = 1

        for i in range(m):  ## preprocessing
            for j in range(n):
                if grid[i][j] == 1:
                    parent[(i, j)] = (i, j)
                    size[(i, j)] = 1
                    if i == 0:
                        union((-1, -1), (i, j))

        for i in range(m):  ## union in the final phase
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in [[1, 0], [0, 1]]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            union((i, j), (ni, nj))

        res = []
        for i, j in hits[::-1]:
            grid[i][j] += 1
            if grid[i][j] == 0:
                res.append(0)
                continue
            if grid[i][j] == 1:
                pre_size = size[find((-1, -1))]
                parent[(i, j)] = (i, j)
                size[(i, j)] = 1
                if i == 0:
                    union((-1, -1), (i, j))
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        union((i, j), (ni, nj))
                post_size = size[find((-1, -1))]
                res.append(max(post_size - pre_size - 1, 0))
        res.reverse()
        return res