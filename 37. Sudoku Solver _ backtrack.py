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


## time - less than (9!)**9, space - O(9**2
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rows = [set(range(1, n + 1)) for _ in range(n + 1)]
        cols = [set(range(1, n + 1)) for _ in range(n + 1)]
        boxes = [set(range(1, n + 1)) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[j // 3 + (i // 3) * 3].remove(num)
        self.dfs(0, rows, cols, boxes, board)

    def dfs(self, curr, rows, cols, boxes, board):
        if curr == 9 * 9:
            return True
        r, c = curr // 9, curr % 9
        b = c // 3 + (r // 3) * 3
        if board[r][c] != '.':
            return self.dfs(curr + 1, rows, cols, boxes, board)

        candidates = rows[r] & cols[c] & boxes[b]
        for num in candidates:
            board[r][c] = str(num)
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[b].remove(num)
            if self.dfs(curr + 1, rows, cols, boxes, board):
                return True
            board[r][c] = '.'
            rows[r].add(num)
            cols[c].add(num)
            boxes[b].add(num)
        return False