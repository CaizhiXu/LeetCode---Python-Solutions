## time - less than (9!)**9
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        limit = len(board) * len(board[0])
        return self.dfs(0, limit, board)

    def dfs(self, curr, limit, board):
        while curr < limit and board[curr // 9][curr % 9] != '.':
            curr += 1
        if curr == limit:
            return True

        r, c = curr // 9, curr % 9
        sr, sc = r // 3, c // 3  # 3x3 square index
        candidates = set([str(i) for i in range(1, 10)])
        for i in range(9):
            if board[r][i] in candidates:
                candidates.remove(board[r][i])
            if board[i][c] in candidates:
                candidates.remove(board[i][c])
            if board[3 * sr + i // 3][3 * sc + i % 3] in candidates:
                candidates.remove(board[3 * sr + i // 3][3 * sc + i % 3])

        for num in candidates:
            board[r][c] = num
            if self.dfs(curr, limit, board):
                return True
            board[r][c] = '.'
        return False