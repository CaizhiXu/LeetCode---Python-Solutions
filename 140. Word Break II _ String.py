## time - O(n**2*n), space - O(n**3)
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = defaultdict(list)
        wordDict = set(wordDict)
        res = self.dfs(s, wordDict, memo)
        return list(map(' '.join, res))

    def dfs(self, s, wordDict, memo):
        if not s:
            return [[]]
        if s in memo:
            return memo[s]

        res = []
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                tmp = self.dfs(s[i + 1:], wordDict, memo)
                for t in tmp:
                    res.append([s[:i + 1]] + t)

        memo[s] = res
        return res