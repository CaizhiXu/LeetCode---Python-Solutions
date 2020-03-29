## time, space - O(n*n)
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    res = max(res, grid[i][j] + self.dfs(i, j, grid))
        return res

    def dfs(self, x, y, grid):
        temp, grid[x][y] = grid[x][y], 0
        res = 0
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny]:
                res = max(res, grid[nx][ny] + self.dfs(nx, ny, grid))
        grid[x][y] = temp
        return res