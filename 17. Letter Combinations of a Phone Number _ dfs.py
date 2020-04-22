class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLett = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return []
        res = []
        self.dfs([], 0, digits, res, numToLett)
        return res

    def dfs(self, path, index, digits, res, numToLett):
        if index == len(digits):
            res.append(''.join(path))
            return
        d = digits[index]
        for ch in numToLett[d]:
            self.dfs(path + [ch], index + 1, digits, res, numToLett)