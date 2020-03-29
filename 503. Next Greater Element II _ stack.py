## time - O(N), space - O(N)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        stack , res = [], [-1]*length
        for i, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                res[stack.pop()[1]] = num
            stack.append((num, i))
        n, start = len(stack), 0
        while n > 1:
            while start < length and nums[start] <= stack[-1][0]:
                start += 1
            if start == length:
                break
            res[stack.pop()[1]] = nums[start]
            n -= 1
        return res