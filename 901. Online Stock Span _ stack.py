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



class StockSpanner2:

    def __init__(self):
        self.stack = [(-1, float('inf'))]
        self.cnt = 0

    def next(self, price: int) -> int:
        while self.stack[-1][1] <= price:
            self.stack.pop()
        res = self.cnt - self.stack[-1][0]
        self.stack.append((self.cnt, price))
        self.cnt += 1
        return res