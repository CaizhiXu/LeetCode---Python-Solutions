## stack
class Solution1:
    def calculate(self, s: str) -> int:
        stack, operand = [], 0
        sign = '+'
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                operand = 10 * operand + int(ch)
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if ch == '(':
                    stack.append(sign)
                    sign = '+'
                    continue
                elif ch == ')':
                    self.helper(sign, operand, stack)
                    operand = 0
                    curr = stack.pop()
                    while isinstance(curr, int):
                        operand += curr
                        curr = stack.pop()
                    sign = curr

                self.helper(sign, operand, stack)
                operand, sign = 0, ch
        return sum(stack)

    def helper(self, sign, operand, stack):
        if sign == '+':
            stack.append(operand)
        elif sign == '-':
            stack.append(-operand)
        elif sign == '*':
            num = stack.pop()
            stack.append(num * operand)
        elif sign == '/':
            num = stack.pop()
            if num // operand < 0 and num % operand != 0:
                stack.append(num // operand + 1)
            else:
                stack.append(num // operand)


## recursion
## recursion
class Solution2:
    def calculate(self, s: str) -> int:
        stack = []
        s = s + '$'
        self.helper(stack, s, 0)
        print(stack)
        return sum(stack)

    def helper(self, stack, s, i):
        operand, sign = 0, '+'
        while i < len(s):
            if s[i].isdigit():
                operand = 10 * operand + int(s[i])
                i += 1
                continue
            if s[i] == ' ':
                i += 1
                continue
            if s[i] == '(':
                operand, i = self.helper([], s, i + 1)
            else:
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                elif sign == '*':
                    stack.append(operand * stack.pop())
                elif sign == '/':
                    stack.append(int(stack.pop() / operand))
                if s[i] == ')':
                    return sum(stack), i + 1
                sign, operand = s[i], 0
                i += 1