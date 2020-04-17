## time, space - O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left_pro = [0] * len(prices)
        right_pro = [0] * len(prices)
        left_min = prices[0]
        right_max = prices[-1]

        for i in range(1, len(prices)):
            left_min = min(left_min, prices[i])
            left_pro[i] = max(left_pro[i - 1], prices[i] - left_min)

            r_idx = len(prices) - 1 - i
            right_max = max(right_max, prices[r_idx])
            right_pro[r_idx] = max(right_pro[r_idx + 1], \
                                   right_max - prices[r_idx])

        maxPro = max(left_pro[-1], right_pro[0])  ## one time sell
        for i in range(len(prices) - 1):
            maxPro = max(maxPro, left_pro[i] + right_pro[i + 1])
        return maxPro