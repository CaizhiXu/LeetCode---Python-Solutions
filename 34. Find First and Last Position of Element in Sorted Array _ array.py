## time - O (logn), space - O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx = [-1, -1]
        if not nums:
            return idx

        idx[0] = self.binarySearch_lower(nums, target)
        idx[1] = self.binarySearch_lower(nums, target + 1) - 1
        if idx[0] < len(nums) and nums[idx[0]] == target:
            return idx
        else:
            return [-1, -1]

    def binarySearch_lower(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left