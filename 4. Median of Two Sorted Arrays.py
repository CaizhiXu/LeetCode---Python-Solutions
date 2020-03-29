## time - O(logm), space - O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            idx1 = left + (right - left) // 2
            idx2 = (m + n) // 2 - idx1

            a = nums1[idx1 - 1] if idx1 > 0 else -float('inf')
            b = nums1[idx1] if idx1 < m else float('inf')
            c = nums2[idx2 - 1] if idx2 > 0 else -float('inf')
            d = nums2[idx2] if idx2 < n else float('inf')

            if a <= d and c <= b:
                if (m + n) % 2 == 1:
                    return min(b, d)
                else:
                    return (max(a, c) + min(b, d)) / 2
            elif a > d:
                right = idx1 - 1
            else:
                left = idx1 + 1