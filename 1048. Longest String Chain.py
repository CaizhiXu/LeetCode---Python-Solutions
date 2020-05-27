##time - O(nll), space - O(n)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        memo = {}
        words = set(words)
        res = 0
        for w in words:
            self.dfs(w, words, memo)
            res = max(res, memo[w])
        return res

    def dfs(self, w, words, memo):
        if w in memo:
            return
        memo[w] = 1
        for i in range(len(w)):
            tmp = w[:i] + w[i + 1:]
            if tmp in words:
                self.dfs(tmp, words, memo)
                memo[w] = max(memo[w], memo[tmp] + 1)
        return