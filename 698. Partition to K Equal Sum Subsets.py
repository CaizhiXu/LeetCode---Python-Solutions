class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k

        visited = {}
        return self.dfs(0, 0, visited, nums, target, total)

    def dfs(self, currSum, state, visited, nums, target, total):
        if currSum == total:
            visited[state] = True
            return True
        if state in visited:
            return visited[state]
        for i, num in enumerate(nums):
            if ((state >> i) & 1 == 0) and num <= target - currSum % target:
                if self.dfs(currSum + num, state | (1 << i), visited, nums, target, total):
                    visited[state] = True
                    return True
        visited[state] = False
        return False



class Solution1(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target: return False

        dp = [False] * (1 << len(nums))
        dp[0] = True
        total = [0] * (1 << len(nums))

        for state in range(1 << len(nums)):
            if not dp[state]: continue
            for i, num in enumerate(nums):
                future = state | (1 << i)
                if state != future and not dp[future]:
                    if (num <= target - (total[state] % target)):
                        dp[future] = True
                        if future == len(dp)-1:
                            return True
                        total[future] = total[state] + num
                    else:
                        break
        return dp[-1]


nums = [4, 3, 2, 2, 5]
k = 2
print(Solution1().canPartitionKSubsets(nums, k))


"""
used = 0, todo = 20
    used = 1, todo = 16
        used = 65, todo = 0


"""

