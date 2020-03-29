## time - (k*m*n), space - O(mn)
from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist_tot = [[0] * n for i in range(m)]
        seenBy = [[0] * n for i in range(m)]
        num_houses = sum([val for row in grid for val in row if val == 1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(i, j, m, n, dist_tot, seenBy, grid)

        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and seenBy[i][j] == num_houses:
                    min_dist = min(min_dist, dist_tot[i][j])
        if min_dist == float('inf'):
            return -1
        return min_dist

    def bfs(self, i, j, m, n, dist_tot, seenBy, grid):
        visited = set()
        dq = deque()
        dq.append((i, j, 0))
        visited.add((i, j))
        while dq:
            x, y, t = dq.pop()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 \
                        and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dq.appendleft((nx, ny, t + 1))
                    dist_tot[nx][ny] += t + 1
                    seenBy[nx][ny] += 1