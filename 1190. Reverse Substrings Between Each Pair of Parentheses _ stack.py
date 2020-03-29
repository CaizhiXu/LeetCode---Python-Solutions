## time - O(n^2)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                temp = ''
                curr = stack.pop()
                while curr != "(":
                    temp += curr
                    curr = stack.pop()
                for ch in temp:
                    stack.append(ch)
            else:
                stack.append(c)
        return "".join(stack)

