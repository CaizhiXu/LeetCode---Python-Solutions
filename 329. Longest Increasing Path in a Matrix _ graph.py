## time, space - O(mn)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        length = [[0] * n for i in range(m)]
        maxLen = 0

        for i in range(m):
            for j in range(n):
                currLen = self.dfs(i, j, m, n, matrix, length)
                maxLen = max(maxLen, currLen)
        return maxLen

    def dfs(self, x, y, m, n, matrix, length):
        if length[x][y] != 0:
            return length[x][y]

        res = 1
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                res = max(res, 1 + self.dfs(nx, ny, m, n, \
                                            matrix, length))
        length[x][y] = res
        return res