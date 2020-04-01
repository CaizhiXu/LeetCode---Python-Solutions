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


## time - O(n), space - o(n)
class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[-1] * i)
        numbers = [i + 1 for i in range(n)]

        path = []
        self.dfs(path, k, n, numbers, factorials)
        return ''.join(path)

    def dfs(self, path, k, n, numbers, factorials):
        if n == 0:
            return
        tmp = (k - 1) // factorials[n - 1]
        k = (k - 1) % factorials[n - 1] + 1
        path += [str(numbers[tmp])]
        self.dfs(path, k, n - 1, numbers[:tmp] + numbers[tmp + 1:], factorials)