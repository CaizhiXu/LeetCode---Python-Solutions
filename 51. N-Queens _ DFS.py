## time ~ O(n!), space - O(n)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        res = []
        visited_col, visited_d1, visited_d2 = set(), set(), set()
        self.dfs(0, n, visited_col, visited_d1, visited_d2, board, res)
        return res

    def dfs(self, row, n, visited_col, visited_d1, visited_d2, board, res):
        if row == n:
            res.append([''.join(row) for row in board])
            return
        for col in range(n):
            if col not in visited_col and (col - row) not in visited_d1 \
                    and (col + row) not in visited_d2:
                board[row][col] = 'Q'
                visited_col.add(col)
                visited_d1.add(col - row)
                visited_d2.add(col + row)
                self.dfs(row + 1, n, visited_col, visited_d1, visited_d2, board, res)
                board[row][col] = '.'
                visited_col.remove(col)
                visited_d1.remove(col - row)
                visited_d2.remove(col + row)
