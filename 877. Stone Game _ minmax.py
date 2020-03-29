## dp, time, space - O(n**2)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for i in range(n)]

        for i in range(n):
            dp[i][i] = -piles[i]

        for delta in range(1, n):
            for i in range(n):
                j = i + delta
                if j >= n:
                    break
                if delta % 2 == 1:
                    dp[i][j] = max(dp[i + 1][j] + piles[i], dp[i][j - 1] + piles[j])
                else:
                    dp[i][j] = min(dp[i + 1][j] - piles[i], dp[i][j - 1] - piles[j])
        return dp[0][n - 1] > 0


class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        def minmax(s, e, turn):
            if s == e:
                return piles[s] * turn
            if (s, e) in memo:
                return memo[(s, e)]
            left = piles[s] * turn + minmax(s + 1, e, -1 * turn)
            right = piles[e] * turn + minmax(s, e - 1, -1 * turn)
            if turn > 0:
                ans = max(left, right)
            else:
                ans = min(left, right)
            memo[(s, e)] = ans
            return ans

        memo = {}
        return minmax(0, len(piles) - 1, 1) > 0