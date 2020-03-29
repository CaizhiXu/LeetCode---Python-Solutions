class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0, 0, res, [], target, candidates)
        return res

    def dfs(self, curr, index, res, path, target, candidates):
        if curr == target:
            res.append(path)
            return
        if index >= len(candidates):
            return
        cnt = 0
        while curr + candidates[index] * cnt <= target:
            self.dfs(curr + candidates[index] * cnt, index + 1, res, path + \
                     [candidates[index]] * cnt, target, candidates)
            cnt += 1