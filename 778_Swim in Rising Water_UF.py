## time, space - O(N*N)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
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

        m, n = len(grid), len(grid[0])
        parent, size, elev_pos = {}, {}, {}
        for i in range(m):
            for j in range(n):
                parent[(i, j)] = (i, j)
                size[(i, j)] = 1
                elev_pos[grid[i][j]] = (i, j)

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for elev in range(m * n):
            x, y = elev_pos[elev]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] < elev:
                    union((nx, ny), (x, y))
                    if find((0, 0)) == find((m - 1, n - 1)):
                        return elev