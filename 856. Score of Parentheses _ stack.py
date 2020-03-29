## time, space - O(N)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for ch in S:
            if ch == "(":
                stack.append(ch)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    val = 0
                    while stack[-1] != "(":
                        val += stack.pop()
                    stack.pop()
                    stack.append(2*val)
        return sum(stack)