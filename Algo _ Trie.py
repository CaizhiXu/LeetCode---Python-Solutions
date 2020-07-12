from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True


class Solution:
    def wordBreak(self, s, wordDict):
        trie = Trie()
        for w in wordDict:
            trie.addWord(w)

        path, res = [], []
        self.dfs(path, s, trie, res)
        return res

    def dfs(self, path, s, trie, res):
        if not s:
            res.append(' '.join(path))
            return

        curr = trie.root
        for i, c in enumerate(s):
            if c in curr.children:
                curr = curr.children[c]
                if curr.is_word:
                    self.dfs(path + [s[:i + 1]], s[i + 1:], trie, res)
            else:
                break


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
sol = Solution()
print(sol.wordBreak(s, wordDict))


