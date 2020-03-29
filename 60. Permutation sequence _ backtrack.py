## time - O(n**2), space - o(n)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [i for i in range(1, n + 1)]
        res = ''
        k -= 1
        while n > 0:
            n -= 1
            fac = self.factorial(n)
            index, k = k // fac, k % fac
            res += str(numbers[index])
            numbers.remove(numbers[index])
        return res

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)