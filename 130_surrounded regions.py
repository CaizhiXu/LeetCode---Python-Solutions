from collections import deque
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    if board[x][y] == 'O' and (x, y) not in visited:
                        dfs(x, y)

        def bfs(i,j):
            que = deque()
            que.appendleft((i,j))
            while que:
                ix, iy = que.pop()
                visited.add((ix, iy))
                for x, y in [[ix + 1, iy], [ix - 1, iy], [ix, iy + 1], [ix, iy - 1]]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]):
                        if board[x][y] == 'O' and (x, y) not in visited:
                            que.appendleft((x,y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    if board[i][j] == 'O' and (i,j) not in visited:
                        dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'

sol = Solution()
board = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
sol.solve(board)
print(board)