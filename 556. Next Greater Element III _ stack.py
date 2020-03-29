## time, space - O(logn)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = [-float('inf')]
        found = False
        while n > 0:
            num = n % 10
            n = n // 10
            if num < stack[-1]:
                found = True
                break
            stack.append(num)

        if not found:
            return -1
        for j in range(len(stack) - 1, -1, -1):
            if stack[j] <= num:
                break
        stack[j + 1], num = num, stack[j + 1]
        res = n * 10 + num

        for j in range(1, len(stack)):
            res = res * 10 + stack[j]
        return res if res <= 2 ** 31 - 1 else -1