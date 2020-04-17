## time - O(logn), space - O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if mid+1<len(nums) and nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left