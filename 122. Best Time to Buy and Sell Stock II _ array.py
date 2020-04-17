## time - O(n), space - O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        if not prices:
            return 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                maxPro += prices[i] - prices[i-1]
        return maxPro