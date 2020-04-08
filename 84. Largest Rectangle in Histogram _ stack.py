## time, space - O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                j = stack.pop()
                left = stack[-1] if stack else -1
                maxA = max(maxA, heights[j] * (i - left - 1))
            stack.append(i)

        right = len(heights)
        while stack:
            j = stack.pop()
            left = stack[-1] if stack else -1
            maxA = max(maxA, heights[j] * (right - left - 1))
        return maxA