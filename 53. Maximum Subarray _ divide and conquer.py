## divide and conquer, time - O(N)
class Solution:
    def maxSubArray(self, nums):
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
    def maxSubArray(self, nums):
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


## time - o(n), space - O(1)
class Solution2:
    def maxSubArray(self, nums):
        """
        i, max local currSum ending at i
        update golbal maxSum
        """
        if not nums:
            return 0
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], nums[i] + currSum)
            maxSum = max(maxSum, currSum)
        return maxSum

    def maxSubArray_index(self, nums):
        """
        start: the start index of currSum ending at i
        currSum: [start, i]
        """
        if not nums:
            return []
        currSum = nums[0]
        currIdx = [0, 0]

        maxSum = nums[0]
        res = [0, 0]
        start = 0

        for i in range(1, len(nums)):
            if currSum > 0:  ## if currSum at i-1 is positive
                currSum = currSum + nums[i]
                currIdx[1] = i
            else:
                currSum = nums[i]
                currIdx = [i, i]
            if currSum > maxSum:
                res = [j for j in currIdx]
                maxSum = currSum
        return res

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution2().maxSubArray(nums))
    print(Solution2().maxSubArray_index(nums))