class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        cnts = [1 for i in range(n)]
        prev = [-1 for i in range(n)]
        nums.sort()
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0 and cnts[j]+1 > cnts[i]:
                    cnts[i] = cnts[j]+1
                    prev[i] = j
        idx = 0
        for i in range(n):
            if cnts[i] > cnts[idx]:
                idx = i
        res = []
        while idx >= 0:
            res.append(nums[idx])
            idx = prev[idx]
        return res