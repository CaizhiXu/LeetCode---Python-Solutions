## time - O(5**(n/2)), space - O(n)
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        _map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        path = [''] * n
        res = []
        self.dfs(path, res, 0, n, _map)
        return res

    def dfs(self, path, res, i, n, _map):
        if i > n - 1 - i:
            res.append(''.join(path))
            return
        if i == n - 1 - i:
            for c in ['0', '1', '8']:
                path[i] = c
                self.dfs(path, res, i + 1, n, _map)
        else:
            for c in _map:
                if i == 0 and c == '0':
                    continue
                path[i] = c
                path[n - 1 - i] = _map[c]
                self.dfs(path, res, i + 1, n, _map)

