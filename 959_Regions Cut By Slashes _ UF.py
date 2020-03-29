## time, space - O(n*n)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        root = [i for i in range(4 * n * n)]

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX

        for i in range(n):
            for j in range(n):
                t, r, b, l = 4 * (i * n + j), 4 * (i * n + j) + 1, 4 * (i * n + j) + 2, 4 * (i * n + j) + 3
                if grid[i][j] == ' ':
                    union(t, r)
                    union(t, b)
                    union(t, l)
                elif grid[i][j] == '/':
                    union(t, l)
                    union(b, r)
                else:
                    union(t, r)
                    union(b, l)
                if i + 1 < n:
                    union(4 * (i * n + j) + 2, 4 * ((i + 1) * n + j))
                if j + 1 < n:
                    union(4 * (i * n + j) + 1, 4 * (i * n + j + 1) + 3)

        return len(set([find(i) for i in range(4 * n * n)]))