## time - O(n), space - O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        n = len(height)
        left, right = 0, n-1
        while left < right:
            left_h = height[left]
            right_h = height[right]
            if left_h <= right_h:
                while left < right and left_h >= height[left]:
                    vol += left_h - height[left]
                    left += 1
            else:
                while right_h >= height[right]:
                    vol += right_h - height[right]
                    right -= 1
        return vol