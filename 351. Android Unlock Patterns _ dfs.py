## time, space - O(A(9, n))
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {}
        skip[(1, 3)] = 2
        skip[(4, 6)] = 5
        skip[(7, 9)] = 8
        skip[(1, 7)] = 4
        skip[(2, 8)] = 5
        skip[(3, 9)] = 6
        skip[(1, 9)] = 5
        skip[(3, 7)] = 5

        self.res = 0
        for i in range(1, 10):
            path = set()
            path.add(i)
            self.dfs(path, i, skip, m, n)
        return self.res

    def dfs(self, path, last, skip, m, n):
        if len(path) >= m:
            self.res += 1
        if len(path) == n:
            return
        for nxt in range(1, 10):
            if nxt in path:
                continue
            edge = (min(last, nxt), max(last, nxt))
            if edge not in skip or skip[edge] in path:
                path.add(nxt)
                self.dfs(path, nxt, skip, m, n)
                path.remove(nxt)