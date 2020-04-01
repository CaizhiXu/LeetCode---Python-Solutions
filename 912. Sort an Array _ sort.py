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


## time - O(nlogn), space - O(n), mergeSort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        nums[k:] = left[i:] or right[j:]
        return nums