## time - O(1), space - O(n)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.dim = n
        self.row, self.col = [0] * n, [0] * n
        self.diag, self.antiDiag = 0, 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            delta = 1
        else:
            delta = -1

        self.row[row] += delta
        self.col[col] += delta
        if row == col:
            self.diag += delta
        if row + col == self.dim - 1:
            self.antiDiag += delta
        if self.dim in [self.row[row], self.col[col], self.diag, self.antiDiag]:
            return 1
        if -self.dim in [self.row[row], self.col[col], self.diag, self.antiDiag]:
            return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)