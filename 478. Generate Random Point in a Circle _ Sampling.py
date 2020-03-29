import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.center = [x_center, y_center]

    def randPoint(self) -> List[float]:
        while True:
            a = random.uniform(-self.radius, self.radius)
            b = random.uniform(-self.radius, self.radius)
            if a ** 2 + b ** 2 <= (self.radius) ** 2:
                return [a + self.center[0], b + self.center[1]]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()