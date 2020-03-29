class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr:
            return 0
        stack = [float('inf')]  # decreasing stack
        res = 0

        for num in arr:
            while stack[-1] <= num:
                local_min = stack.pop()
                res += local_min * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res