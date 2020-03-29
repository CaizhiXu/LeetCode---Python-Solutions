## time, space - O(3**n)
from collections import defaultdict


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numToLett = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        res = []
        self.dfs(0, len(digits), '', res, numToLett, digits)
        return res

    def dfs(self, i, n, curr, res, dct, digits):
        if i == n:
            res.append(curr)
            return
        for c in dct[digits[i]]:
            self.dfs(i + 1, n, curr + c, res, dct, digits)