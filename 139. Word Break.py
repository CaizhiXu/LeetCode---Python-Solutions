## time - O(n**2), space - O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        wordSet = set(wordDict)
        memo = {}
        return self.dfs(s, 0, wordSet, memo)

    def dfs(self, s, i, wordSet, memo):
        if i == len(s):
            memo[i] = True
            return True
        if i in memo:
            return memo[i]

        for j in range(i, len(s)):
            if s[i:j + 1] in wordSet:
                if self.dfs(s, j + 1, wordSet, memo):
                    memo[i] = True
                    return True
        memo[i] = False
        return False