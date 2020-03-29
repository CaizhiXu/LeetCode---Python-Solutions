class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        if not S:
            return res
        self.dfs(0, len(S) - 1, '', res, S)
        return res

    def dfs(self, i, j, curr, res, S):
        if i > j:
            res.append(curr)
            return
        if S[i].isdigit():
            self.dfs(i + 1, j, curr + S[i], res, S)
        else:
            self.dfs(i + 1, j, curr + S[i].lower(), res, S)
            self.dfs(i + 1, j, curr + S[i].upper(), res, S)