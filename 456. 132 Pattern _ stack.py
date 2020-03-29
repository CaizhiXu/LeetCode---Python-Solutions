## time, sapce - O(N)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [float("inf")]
        pivot = -float("inf")
        for num in nums[-1::-1]:
            if num < pivot:
                return True
            while num > stack[-1]:
                pivot = stack.pop()
            stack.append(num)
        return False