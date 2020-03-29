## time, space - O(N)
class StockSpanner:

    def __init__(self):
        self.prices = [(float('inf'), 0)]  # decreasing stack

    def next(self, price: int) -> int:
        if price < self.prices[-1][0]:
            self.prices.append((price, 1))
            return 1
        count = 1
        while price >= self.prices[-1][0]:
            count += self.prices.pop()[1]
        self.prices.append((price, count))
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)