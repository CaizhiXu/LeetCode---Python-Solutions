## time, space - O(2**N)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(path, arr):
            if not arr:
                res.append(path)
                return
            for i, num in enumerate(arr):
                helper(path + [num], arr[:i] + arr[i + 1:])

        res = []
        helper([], nums)
        return res


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums, cur, visited, res):
            if len(cur) == len(nums):
                res.append(cur)
                return
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    dfs(nums, cur + [nums[i]], visited, res)
                    visited.remove(i)

        visited = set()
        dfs(nums, [], visited, res)
        return res


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums, cur, res):
            if len(cur) == len(nums):
                res.append(cur)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], cur + [nums[i]], res)

        visited = set()
        dfs(nums, [], res)
        return res

