class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        turn = 0
        m, n = len(matrix), len(matrix[0])

        for turn in range(m + n - 1):
            if turn % 2 == 0:
                i = min(turn, m - 1)
                j = turn - i
                step = [-1, 1]
            else:
                j = min(turn, n - 1)
                i = turn - j
                step = [1, -1]
            while 0 <= i < m and 0 <= j < n:
                res.append(matrix[i][j])
                i += step[0]
                j += step[1]
        return res