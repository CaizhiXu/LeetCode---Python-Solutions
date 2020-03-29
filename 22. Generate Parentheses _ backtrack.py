## time, space - O(n**2)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        self.dfs(n, n, '', res)
        return res

    def dfs(self, l, r, curr, res):
        if l == 0 and r == 0:
            res.append(curr)
            return
        if l == r:
            self.dfs(l - 1, r, curr + '(', res)
        elif l == 0:
            self.dfs(l, r - 1, curr + ')', res)
        else:
            self.dfs(l - 1, r, curr + '(', res)
            self.dfs(l, r - 1, curr + ')', res)