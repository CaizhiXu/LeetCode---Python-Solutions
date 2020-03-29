# time - log(n), space - O(1)
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = self.lcm(a, b)
        bc = self.lcm(b, c)
        ca = self.lcm(c, a)
        abc = self.lcm(ca, b)

        def f(num):
            return num // a + num // b + num // c - num // ab - num // bc - num // ca + num // abc

        left = min(a, b, c)
        right = left * n
        while left < right:
            mid = left + (right - left) // 2
            if f(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left

    def gcd(self, a, b):  ## Euclid algorithm
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return (a * b) / self.gcd(a, b)