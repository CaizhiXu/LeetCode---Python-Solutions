## time, space - O(MN)
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for i in range(m)]
        nxt_lvl = []
        dep = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n and dp[x][y] == float('inf')):
                return
            nxt_lvl.append((x, y))
            dp[x][y] = dep
            dfs(x + dirs[grid[x][y] - 1][0], y + dirs[grid[x][y] - 1][1])

        dfs(0, 0)
        while nxt_lvl:
            dep += 1
            curr_lvl, nxt_lvl = nxt_lvl, []
            for x, y in curr_lvl:
                for dx, dy in dirs:
                    dfs(x + dx, y + dy)
        return dp[-1][-1]


## time - O(MN + MNlongMN), space - O(MN)， dijkstra
import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        hq = []
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for i in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        hq = [(0, 0, 0)]
        dp[0][0] = 0
        while hq:
            cost, x, y = heapq.heappop(hq)
            if x == m - 1 and y == n - 1:
                return cost
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if dirs[grid[x][y] - 1] == [dx, dy]:
                        newCost = cost
                    else:
                        newCost = cost + 1
                    if newCost < dp[nx][ny]:
                        dp[nx][ny] = newCost
                        heapq.heappush(hq, (newCost, nx, ny))