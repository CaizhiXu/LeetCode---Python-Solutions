## time - O(2**n), space - (C(n, n/2))
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        dq = deque([s])
        visited = set()
        visited.add(s)
        res = []
        found = False

        while dq:
            curr = dq.pop()
            print(curr)
            if self.isValid(curr):
                found = True
                res.append(curr)
            if found:
                continue

            for i, c in enumerate(curr):
                if c == '(' or c == ')':
                    nxt = curr[:i] + curr[i + 1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        dq.appendleft(nxt)
        return res

    def isValid(self, string):
        if not string:
            return True
        cnt = 0
        for c in string:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    return False
                cnt -= 1
        return cnt == 0