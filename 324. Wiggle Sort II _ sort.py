## time, space - O(N)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        m = (n + 1) // 2
        median = self.quickSelect(nums, m)
        arr = [i for i in nums]

        l, r = 0, n - 1
        idx = l
        while l < r:
            if arr[l] < median:
                arr[l], arr[idx] = arr[idx], arr[l]
                idx += 1
                l += 1
            elif arr[l] > median:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
            else:
                l += 1
        j, k = m - 1, n - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = arr[j]
                j -= 1
            else:
                nums[i] = arr[k]
                k -= 1

    def quickSelect(self, arr, k):
        start, end = 0, len(arr) - 1
        while start <= end:
            if start == end:
                return arr[start]
            l, r = start, end
            low = l
            mid = l + (r - l) // 2
            arr[mid], arr[r] = arr[r], arr[mid]
            while l < r:
                if arr[l] < arr[r]:
                    arr[l], arr[low] = arr[low], arr[l]
                    low += 1
                l += 1
            arr[low], arr[r] = arr[r], arr[low]
            if low + 1 > k:
                end = low - 1
            elif low + 1 < k:
                start = low + 1
            else:
                return arr[low]


## time - O(N), space - O(1)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        m = (n + 1) // 2
        median = self.quickSelect(nums, m)

        def A(i):
            return (2 * i + 1) % (n | 1)

        l, r = 0, n - 1
        j = l
        while l <= r:
            if nums[A(l)] < median:
                nums[A(l)], nums[A(r)] = nums[A(r)], nums[A(l)]
                r -= 1
            elif nums[A(l)] > median:
                nums[A(l)], nums[A(j)] = nums[A(j)], nums[A(l)]
                j += 1
                l += 1
            else:
                l += 1

    def quickSelect(self, arr, k):
        start, end = 0, len(arr) - 1
        while start <= end:
            if start == end:
                return arr[start]
            l, r = start, end
            low = l
            mid = l + (r - l) // 2
            arr[mid], arr[r] = arr[r], arr[mid]
            while l < r:
                if arr[l] < arr[r]:
                    arr[l], arr[low] = arr[low], arr[l]
                    low += 1
                l += 1
            arr[low], arr[r] = arr[r], arr[low]
            if low + 1 > k:
                end = low - 1
            elif low + 1 < k:
                start = low + 1
            else:
                return arr[low]