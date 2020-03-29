## time - O(klog*mn), space - O(mn)
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        root = {}
        size = {}
        grid = [[0] * n for i in range(m)]
        res, num = [], 0

        for x, y in positions:
            if grid[x][y] == 1:
                res.append(num)
                continue
            grid[x][y] = 1
            root[(x, y)] = (x, y)
            size[(x, y)] = 1
            islands = set()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    islands.add(self.find((nx, ny), root))
            num += 1 - len(islands)
            res.append(num)

            for isl in islands:
                self.union((x, y), isl, root, size)
        return res

    def find(self, pos, root):
        if root[pos] != pos:
            root[pos] = self.find(root[pos], root)
        return root[pos]

    def union(self, a, b, root, size):
        root_a = self.find(a, root)
        root_b = self.find(b, root)
        if root_a != root_b:
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            root[root_b] = root_a
            size[root_a] += size[root_b]