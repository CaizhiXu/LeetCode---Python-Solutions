## time - O(n), space - O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            limit = min(len(nums) - 1, i + nums[i])
            if pos <= limit:
                pos = i

        return pos == 0


## DP, bottom up
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            limit = min(len(nums) - 1, i + nums[i])
            for j in range(limit, i, -1):
                if dp[j] == True:
                    dp[i] = True
                    break

        return dp[0]

## DP, top down
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def helper(i):
            if i == len(nums) - 1:
                return True
            if i in memo:
                return memo[i]

            limit = min(len(nums) - 1, i + nums[i])
            for j in range(limit, i, -1):
                if helper(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return helper(0)