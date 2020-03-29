## time - O(N), space - O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            cnt = 1
            while i < len(nums)-1 and nums[i] < nums[i+1]:
                cnt += 1
                i += 1
            res = max(res, cnt)
            i += 1
        return res