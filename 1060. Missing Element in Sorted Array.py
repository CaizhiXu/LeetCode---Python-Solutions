## time - O(logn), space - O(1)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.numMiss(mid, nums) < k <= self.numMiss(mid + 1, nums):
                l = mid
                break
            elif k <= self.numMiss(mid, nums):
                r = mid
            else:
                l = mid + 1
        return nums[l] + (k - self.numMiss(l, nums))

    def numMiss(self, idx, arr):
        return (arr[idx] - arr[0]) - idx
