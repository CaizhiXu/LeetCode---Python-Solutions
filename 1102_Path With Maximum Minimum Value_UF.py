## time - O(MN*log(MN)), space - O(MN)
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        r, c = len(A), len(A[0])
        root = [i for i in range(r * c)]
        visited = set()
        cells = [[i, j] for i in range(r) for j in range(c)]
        cells.sort(key=lambda x: A[x[0]][x[1]], reverse=True)

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX

        for x, y in cells:
            visited.add((x, y))
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and (nx, ny) in visited:
                    union(x * c + y, nx * c + ny)
            if find(0) == find(r * c - 1):
                return A[x][y]