class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for c in range(n):
            num = matrix[0][c]
            for r in range(min(m, n - c)):
                if matrix[r][c + r] != num:
                    return False

        for r in range(m):
            num = matrix[r][0]
            for c in range(min(n, m - r)):
                if matrix[r + c][c] != num:
                    return False
        return True