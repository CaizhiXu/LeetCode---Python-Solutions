# time - O(MN), space - O(MN)
class TrieNode:
    def __init__(self, val):
        self.next = {}
        self.isEnd = False
        self.val = val


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode(c)
            node = node.next[c]
        node.isEnd = True

    def bfs(self):
        q = collections.deque([(self.root, "")])
        res = ''
        while q:
            cur, word_sofar = q.pop()
            if len(word_sofar) > len(res) or (len(word_sofar) == len(res) and word_sofar < res):
                res = word_sofar
            for n in cur.next.values():
                if n.isEnd:
                    q.appendleft((n, word_sofar + n.val))
        return res


class Solution:
    def longestWord(self, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.bfs()