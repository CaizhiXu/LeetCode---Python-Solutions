## time - O(mn), space - O(m+n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                curr = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p = (n1 - i - 1) + (n2 - j - 1) + 1
                res[-p] += curr

        carry = 0
        for i in range(len(res) - 1, -1, -1):
            tmp = res[i] + carry
            carry = tmp // 10
            res[i] = tmp % 10

        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        if i == len(res):
            return '0'
        return ''.join(map(str, res[i:]))