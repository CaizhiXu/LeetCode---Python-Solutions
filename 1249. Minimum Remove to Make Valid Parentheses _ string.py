## time - O(n), space - O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid = set()

        def helper(string, open_symbol, close_symbol, reverse=False):
            balance = 0
            for i, c in enumerate(string):
                if c == open_symbol:
                    balance += 1
                elif c == close_symbol:
                    if balance == 0:
                        if not reverse:
                            invalid.add(i)
                        else:
                            invalid.add(n - 1 - i)
                    else:
                        balance -= 1

        n = len(s)
        helper(s, '(', ')')
        helper(s[::-1], ')', '(', reverse=True)

        res = []
        for i, c in enumerate(s):
            if i not in invalid:
                res.append(c)
        return ''.join(res)


## time - O(n), space - O(n)
class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        toRemove = set()
        stack = []  ## stores idx of unmatched "("
        balance = 0

        for i, c in enumerate(s):
            if c == '(':
                balance += 1
                stack.append(i)
            elif c == ')':
                if balance == 0:
                    toRemove.add(i)
                else:
                    stack.pop()
                    balance -= 1
        while stack:
            toRemove.add(stack.pop())

        res = []
        for i, c in enumerate(s):
            if i not in toRemove:
                res.append(c)
        return ''.join(res)
