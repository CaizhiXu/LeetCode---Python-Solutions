## Time - O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(0, len(nums) - 1, nums, k, len(nums))

    def quickSelect(self, start, end, nums, k, N):
        if start == end:
            return nums[start]
        mid = start + (end - start) // 2
        pivot = nums[mid]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= N - left:
            return self.quickSelect(left, end, nums, k, len(nums))
        else:
            return self.quickSelect(start, left - 1, nums, k, len(nums))


## Time - O(n), space - O(logn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = self.partition(nums)
        length = len(nums)
        if k < length - pos:
            return self.findKthLargest(nums[pos + 1:], k)
        elif k > length - pos:
            return self.findKthLargest(nums[:pos], k - length + pos)
        else:
            return nums[pos]

    def partition(self, arr):
        l, r = 0, len(arr) - 1
        mid = l + (r - l) // 2
        ## this choice of pivot can shorten time complexity
        arr[r], arr[mid] = arr[mid], arr[r]
        low = l
        while l < r:
            if arr[l] < arr[r]:
                arr[l], arr[low] = arr[low], arr[l]
                low += 1
            l += 1
        arr[low], arr[r] = arr[r], arr[low]
        return low


## Time - O(n), space - O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(0, len(nums) - 1, nums, k, len(nums))

    def quickSelect(self, start, end, nums, k, N):
        while start <= end:
            if start == end:
                return nums[start]
            l, r = start, end
            mid = l + (r-l)//2
            nums[r], nums[mid] = nums[mid], nums[r]
            low = l
            while l < r:
                if nums[l] < nums[r]:
                    nums[low], nums[l] = nums[l], nums[low]
                    low += 1
                l += 1
            nums[low], nums[r] = nums[r], nums[low]
            if N-low > k:
                start = low + 1
            elif N-low < k:
                end = low - 1


## time - O(n), space - O(1)

1st largest <--> nth smallest
2nd largest <--> (n-1)th smallest

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        n = len(nums)
        while l < r:
            pos = self.partition(nums, l, r)
            if pos == n - k:
                return nums[pos]
            elif pos > n - k:
                r = pos - 1
            else:
                l = pos + 1
        return nums[l]

    def partition(self, nums, l, r):
        rid = random.randint(l, r)
        nums[r], nums[rid] = nums[rid], nums[r]
        j = l
        for i in range(l, r):
            if nums[i] < nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j], nums[r] = nums[r], nums[j]
        return j


"""
after for loop
[s1, j, s2, pivot]
nums[s1] < pivot
nums[j, s2] >= pivot

after the swap before return
[s1, j, s2]
nums[s1] < pivot
nums[j] = pivot
nums[s2] >= pivot


kth smallest number
[1, 2, 3(j), 5, 6, 4,  100]

             [4, 5, 6, 100]
the (j+1) th smallest number in this array is nums[j]

if j+1 == k:
    return nums[j+1]
elif j+1 > k:
    r = j-1
else:
    l = j+1
    
    
   



pivot = 3

j <= i 
nums[j] >= pivot

...j ..... i .....pivot


"""