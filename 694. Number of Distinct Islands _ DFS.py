## time, space - O(MN)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    new_isl = []
                    self.helper(i, j, new_isl, grid)
                    islands.add("".join(new_isl))
        return len(islands)

    def helper(self, x, y, new_isl, grid):
        grid[x][y] = 0
        for dx, dy, d in [(0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd'), (-1, 0, 'u')]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                new_isl.append(d)
                self.helper(nx, ny, new_isl, grid)
        new_isl.append('e')