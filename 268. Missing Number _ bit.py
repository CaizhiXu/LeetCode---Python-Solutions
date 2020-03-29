## time - O(nlogn), space - O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxNum = 0
        for i, num in enumerate(nums):
            maxNum = max(maxNum, num)
            if maxNum != i:
                return i
        return i+1