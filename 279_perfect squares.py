## sol1 - DFS
class Solution:
    def __init__(self):
        self.memo = {}

    def numSquares(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        res = n
        for i in range(int(n ** (0.5)), 0, -1):
            if i ** 2 == n:
                self.memo[n] = 1
                return 1
            res = min(res, 1 + self.numSquares(n - i ** 2))
        self.memo[n] = res
        return res

## sol2 - dp, time - O(n**1.5), space - O(n)
class Solution2(object):
    def numSquares(self, n):
        dp = [i for i in range(n+1)]
        for curr in range(2, int(n**(0.5))+1)
            for j in range(curr*curr,n+1):
                dp[j] = min(dp[j],dp[j-curr*curr]+1)
        return dp[-1]

## sol3 - dp
class Solution3:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]


## sol3 - BFS, fastest solution
class Solution(object):
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        q, res = {n}, 1
        while q:
            sub_q = set()
            for node in q:
                for num in squares:
                    if node == num:
                        return res
                    if node < num:
                        break
                    sub_q.add(node - num)
            q, res = sub_q, res+1


## another bfs, time - O(n), space - O(n**0.5)
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dq = deque([(n, 0)])
        visited = set([n])

        while dq:
            num, dep = dq.pop()
            if num == 0:
                return dep
            for s in squares:
                if s < num:
                    if num - s not in visited:
                        dq.appendleft((num - s, dep + 1))
                        visited.add(num - s)
                elif s == num:
                    return dep + 1
                else:
                    break