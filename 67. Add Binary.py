## time, space - O(n)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a)-1, len(b)-1
        carry = 0
        while i>= 0 or j>=0:
            opA = a[i] if i>=0 else '0'
            opB = b[j] if j>=0 else '0'
            tmp = carry + int(opA) + int(opB)
            carry = tmp//2
            res.append(str(tmp%2))
            i -= 1
            j -= 1
        if carry:
            res.append(str(carry))
        res.reverse()
        return "".join(res)