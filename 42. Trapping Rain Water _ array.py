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



## time - O(n), space - O(n)
class Solution2:
    def trap(self, height: List[int]) -> int:
        vol = 0
        stack = [-1]
        for i, h in enumerate(height):
            while stack[-1] != -1 and height[stack[-1]] < h:
                tmp = stack.pop()
                if stack[-1] == -1:
                    continue
                upper = min(height[stack[-1]], h)
                width = i - stack[-1] -1
                vol += (upper - height[tmp])*width
            stack.append(i)
        return vol