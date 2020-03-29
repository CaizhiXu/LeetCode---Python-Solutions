class Solution:
    def calculate(self, s: str) -> int:
        operand, sign, res = 0, 1, 0
        stack = []

        for ch in s:
            if ch.isdigit():
                operand = 10 * operand + int(ch)
            elif ch in "+-":
                res += sign * operand
                sign = 1 if ch == "+" else -1
                operand = 0
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif ch == ")":
                res += operand * sign
                operand = res
                sign = stack.pop()
                res = stack.pop()
        return res + sign * operand