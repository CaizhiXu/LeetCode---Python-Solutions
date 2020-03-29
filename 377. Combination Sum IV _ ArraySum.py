## time - O(target*N, or Nlog(N)), space - O(target)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = [0] * (target + 1)

        for i in range(1, target + 1):
            for num in nums:
                if i < num:
                    break
                if i == num:
                    res[i] += 1
                elif i > num:
                    res[i] += res[i - num]

        return res[target]

## dfs
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}
        self.dfs(target, memo, nums)
        return memo[target]

    def dfs(self, target, memo, arr):
        if target in memo:
            return memo[target]
        if target == 0:
            memo[target] = 0
            return memo[target]
        res = 0
        for num in arr:
            if num > target:
                break
            if num == target:
                res += 1
            else:
                res += self.dfs(target - num, memo, arr)
        memo[target] = res
        return res