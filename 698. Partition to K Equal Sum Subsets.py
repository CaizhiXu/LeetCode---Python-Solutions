class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k:
            return False
        target = total // k

        visited = {}
        res = []
        self.dfs(0, 0, visited, nums, target, total//k, res)
        return res

    def dfs(self, currSum, state, visited, nums, target, total, res):
        if state in visited:
            return visited[state]
        if currSum == total:
            visited[state] = True
            visited[2**len(nums)-1-state] = True
            res.append(state)
            return True

        for i, num in enumerate(nums):
            if ((state >> i) & 1 == 0) and num <= target - currSum % target:
                if self.dfs(currSum + num, state | (1 << i), visited, nums, target, total, res):
                    visited[state] = True
                    #return True
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


class Solution3:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k:
            return False
        target = total // k

        visited = {}
        res = []
        self.dfs(0, 0, visited, nums, target, total//k, res)
        return res

    def dfs(self, currSum, state, visited, nums, target, total, res):
        if state in visited:
            return visited[state]
        if currSum == total:
            visited[state] = True
            visited[2**len(nums)-1-state] = True
            res.append(state)
            return True

        for i, num in enumerate(nums):
            if ((state >> i) & 1 == 0) and num <= target - currSum % target:
                if self.dfs(currSum + num, state | (1 << i), visited, nums, target, total, res):
                    visited[state] = True
                    #return True
        visited[state] = False
        return False


nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
print(Solution3().canPartitionKSubsets(nums, k))


"""
used = 0, todo = 20
    used = 1, todo = 16
        used = 65, todo = 0


"""

