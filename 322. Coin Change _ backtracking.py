## time - O(MC), space - O(M)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for amn in range(1, amount+1):
            for c in coins:
                if c <= amn:
                    dp[amn] = min(dp[amn], dp[amn-c] + 1)
        return dp[amount] if dp[amount] < amount+1 else -1


## dfs, time - O(MC), space - O(M)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        self.dfs(coins, amount, memo)
        return memo[amount] if memo[amount] < amount + 1 else -1

    def dfs(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            memo[0] = 0
            return 0
        res = float('inf')
        for c in coins:
            if amount >= c:
                res = min(res, 1 + self.dfs(coins, amount - c, memo))
        memo[amount] = res
        return res