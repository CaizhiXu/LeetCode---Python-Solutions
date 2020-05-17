## time - O(n), space - O(1)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        res = 0
        buy, sell = prices[0], prices[0]
        for i, p in enumerate(prices):
            if p < buy or p+fee < sell:
                res += max(0, sell-buy-fee)
                buy, sell = p, p
            else:
                sell = max(sell, p)
        res += max(0, sell-buy-fee)
        return res        