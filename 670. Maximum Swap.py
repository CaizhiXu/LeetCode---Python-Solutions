## time, space - O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [c for c in str(num)]
        if len(digits) <= 1:
            return num

        stack = []
        for i, d in enumerate(digits):
            while stack and digits[stack[-1]] <= d:
                stack.pop()
            stack.append(i)
        i, j = 0, 0
        for i in range(len(digits)):
            if i == stack[j]:
                j += 1
            elif digits[i] == digits[stack[j]]:
                continue
            else:
                digits[i], digits[stack[j]] = digits[stack[j]], digits[i]
                break
        return int(''.join(digits))