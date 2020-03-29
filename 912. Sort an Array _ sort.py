## time- O(nlogn), space - O(logn)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right):
        if right - left < 1:
            return
        l, r = left, right
        mid = l + (r - l) // 2
        nums[mid], nums[r] = nums[r], nums[mid]
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        self.quickSort(nums, left, low - 1)
        self.quickSort(nums, low + 1, right)