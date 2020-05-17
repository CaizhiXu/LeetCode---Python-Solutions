## time - O(nk), space - O(nk)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        if k >= n / 2:
            return self.helper(k, prices)

        dp = [[0] * n for i in range(k + 1)]
        for i in range(1, k + 1):
            tmp = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp)
                tmp = max(tmp, dp[i - 1][j - 1] - prices[j])
        return dp[k][n - 1]

    def helper(self, k, prices):
        res = 0
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res += prices[i + 1] - prices[i]
        return res