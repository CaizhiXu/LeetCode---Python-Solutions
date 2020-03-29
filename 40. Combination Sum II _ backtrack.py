## time, space - O(2**N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(0, 0, [], res, target, candidates)
        return res

    def dfs(self, curr, index, path, res, target, candidates):
        if curr == target:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if curr + candidates[i] <= target:
                self.dfs(curr + candidates[i], i + 1, path + [candidates[i]], \
                         res, target, candidates)