## time - O(nlogn), space - O(n)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        return self.helper(preSum, 0, len(preSum), lower, upper)

    def helper(self, arr, l, r, lower, upper):
        if r - l <= 1:
            return 0
        mid = (l + r) // 2
        count = self.helper(arr, l, mid, lower, upper) \
                + self.helper(arr, mid, r, lower, upper)

        i, j = mid, mid
        for num in arr[l:mid]:
            while i < r and arr[i] - num < lower:
                i += 1
            while j < r and arr[j] - num <= upper:
                j += 1
            count += j - i
        arr[l:r] = sorted(arr[l:r])
        return count


## time - O(nlogn), space - O(n)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        return self.helper(preSum, lower, upper)

    def helper(self, arr, lower, upper):
        n = len(arr)
        if n <= 1:
            return 0
        mid = (n + 1) // 2
        left = arr[:mid]
        right = arr[mid:]
        count = self.helper(left, lower, upper) \
                + self.helper(right, lower, upper)

        i, j = 0, 0
        for num in left:
            while i < n - mid and right[i] - num < lower:
                i += 1
            while j < n - mid and right[j] - num <= upper:
                j += 1
            count += j - i
        arr.sort()
        return count