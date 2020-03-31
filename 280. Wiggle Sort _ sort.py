## time, space - O(n)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = (1 + n) // 2
        self.quickSelect(nums, k)
        nums_copy = [i for i in nums]

        for i in range(k):
            nums[2 * i] = nums_copy[i]
        for i in range(k, n):
            nums[2 * (i - k) + 1] = nums_copy[i]

    def quickSelect(self, arr, k):
        left, right = 0, len(arr) - 1
        while left <= right:
            if left == right:
                return
            l, r = left, right
            mid = l + (r - l) // 2
            arr[r], arr[mid] = arr[mid], arr[r]
            low = l
            while l < r:
                if arr[l] < arr[r]:
                    arr[l], arr[low] = arr[low], arr[l]
                    low += 1
                l += 1
            arr[low], arr[r] = arr[r], arr[low]
            if low + 1 < k:
                left = low + 1
            elif low + 1 > k:
                right = low - 1
            else:
                return


## times - O(n), space - O(1)
class Solution2:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i%2 == 0:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]