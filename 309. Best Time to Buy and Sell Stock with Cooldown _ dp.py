## time - O(n), space - O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        sell, hold, reset
        sell = hold' + p
        hold = max(hold', reset'-p)
        reset = max(reset', sell')
        """
        if not prices:
            return 0
        sell, hold, reset = -float('inf'), -float('inf'), 0

        for p in prices:
            pre_sell = sell
            sell = hold + p
            hold = max(hold, reset - p)
            reset = max(reset, pre_sell)

        return max(sell, reset)