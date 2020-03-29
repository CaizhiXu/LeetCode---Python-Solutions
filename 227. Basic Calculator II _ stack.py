class Solution:
    def calculate(self, s: str) -> int:
        stack, operand = [], 0
        sign = '+'
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                operand = 10*operand + int(ch)
            if (not ch.isdigit() and ch != ' ') or i == len(s)-1:
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                elif sign == '*':
                    num = stack.pop()
                    stack.append(num*operand)
                elif sign == '/':
                    num = stack.pop()
                    if num//operand < 0 and num%operand != 0:
                        stack.append(num//operand + 1)
                    else:
                        stack.append(num//operand)
                operand, sign = 0, ch
        return sum(stack)