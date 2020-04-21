## time - O(n), space - O(1)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        balance = 0
        cnt, res = 0, 0

        for c in s:
            if c == '(':
                balance += 1
            else:
                if balance == 0:
                    cnt = 0
                else:
                    balance -= 1
                    cnt += 1
                    if balance == 0:
                        res = max(res, cnt * 2)

        balance, cnt = 0, 0
        for c in s[::-1]:
            if c == ')':
                balance += 1
            else:
                if balance == 0:
                    cnt = 0
                else:
                    balance -= 1
                    cnt += 1
                    if balance == 0:
                        res = max(res, cnt * 2)
        return res


## time - O(n), space - O(1)
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        stack, res = [-1], 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)  # mark the invalid ')'
        return res