## time - O(n), space - O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry, res = 0, []
        l1, l2 = len(num1), len(num2)

        for i in range(max(l1, l2)):
            i1 = l1 - 1 - i
            i2 = l2 - 1 - i
            n1 = ord(num1[i1]) - ord('0') if i1 >= 0 else 0
            n2 = ord(num2[i2]) - ord('0') if i2 >= 0 else 0
            tmp = carry + n1 + n2
            carry = tmp // 10
            res.append(tmp % 10)
        if carry != 0:
            res.append(carry)

        res.reverse()
        return ''.join(map(str, res))


## consider floats
class Solution2:
    def addStrings(self, num1, num2):
        idx1 = num1.index('.')
        idx2 = num2.index('.')
        start = min(idx1-len(num1)+1, idx2-len(num2)+1)
        end = max(idx1, idx2)

        carry = 0
        res = []
        for i in range(start, end+1):
            if i == 0:
                res.append('.')
                continue
            p1 = idx1 - i
            p2 = idx2 - i
            n1 = ord(num1[p1]) - ord('0') if 0 <= p1 < len(num1) else 0
            n2 = ord(num2[p2]) - ord('0') if 0 <= p2 < len(num2) else 0
            tmp = n1 + n2 + carry
            carry = tmp//10
            res.append(str(tmp%10))
        if carry != 0:
            res.append('1')
        res.reverse()
        return ''.join(res)

sol = Solution2()
num1 = '15.3'
num2 = '999.93'
print(sol.addStrings(num1, num2))


