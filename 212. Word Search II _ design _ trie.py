class TrieNode:
    def __init__(self):
        self.next = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for c in word:
            if c not in root.next:
                root.next[c] = TrieNode()
            root = root.next[c]
        root.isWord = True


## time, space - O(mnl)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs((i, j), board, trie.root, '', res)
        return res

    def dfs(self, pos, board, node, curr, res):
        i, j = pos
        temp = board[i][j]
        if temp not in node.next:
            return
        nxt_node = node.next[temp]
        if nxt_node.isWord:
            res.append(curr + temp)
            nxt_node.isWord = False

        board[i][j] = '#'
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and \
                    board[ni][nj] != '#':
                self.dfs((ni, nj), board, nxt_node, curr + temp, res)
        board[i][j] = temp