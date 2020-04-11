## time - O(n), space - O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = ''
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                first = ord(num1[i]) - ord('0')
            else:
                first = 0
            if j >= 0:
                second = ord(num2[j]) - ord('0')
            else:
                second = 0
            i, j = i - 1, j - 1

            tmp = carry + first + second
            carry = tmp // 10
            res = str(tmp % 10) + res
        if carry:
            res = str(1) + res
        return res