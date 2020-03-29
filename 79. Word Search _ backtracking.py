class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if self.dfs((i, j), 1, board, word, visited):
                        return True
        return False

    def dfs(self, pos, match, board, word, visited):
        visited.add(pos)
        if match == len(word):
            return True
        i, j = pos
        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and \
                    (ni, nj) not in visited:
                if board[ni][nj] == word[match]:
                    if self.dfs((ni, nj), match + 1, board, word, visited):
                        return True
        visited.remove(pos)
        return False

