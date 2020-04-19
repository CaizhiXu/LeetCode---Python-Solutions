## time - O(n), space - O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ''
        path = path.split('/')
        stack = []
        for d in path:
            if not d or d == '.':
                continue
            if d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        res = '/'
        if not stack:
            return res
        return res + '/'.join(stack)