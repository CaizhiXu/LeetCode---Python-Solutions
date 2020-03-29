## divide and conquer, time - O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r, m, s = self.maxSubSum(nums, 0, len(nums) - 1)
        return m

    def maxSubSum(self, arr, left, right):
        if left == right:
            return arr[left], arr[left], arr[left], arr[left]
        mid = left + (right - left) // 2
        l1, r1, m1, s1 = self.maxSubSum(arr, left, mid)
        l2, r2, m2, s2 = self.maxSubSum(arr, mid + 1, right)
        l = max(l1, s1 + l2)
        r = max(r2, s2 + r1)
        m = max(m1, m2, r1 + l2)
        s = s1 + s2
        return l, r, m, s


## dp, time - O(N)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        max_curr = nums[0]
        for i in range(1, len(nums)):
            if max_curr < 0:
                max_curr = nums[i]
            else:
                max_curr += nums[i]
            if maxSum < max_curr:
                maxSum = max_curr
        return maxSum