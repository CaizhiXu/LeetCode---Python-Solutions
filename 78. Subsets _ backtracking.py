## time, space - O(2**N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(i, curr):
            if i == n:
                res.append(curr)
                return
            helper(i+1, curr)
            helper(i+1, curr+[nums[i]])
        helper(0, [])
        return res