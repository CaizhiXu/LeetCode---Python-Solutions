class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            raise ValueError("Denominator can't be zero!")
        if numerator == 0:
            return '0'

        res = []
        if (numerator < 0) != (denominator < 0):
            res.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)

        res.append(str(numerator // denominator))
        tmp = numerator % denominator
        if tmp == 0:
            return "".join(res)

        res.append('.')
        seen = {}
        idx = len(res)
        while tmp > 0:
            seen[tmp] = idx
            tmp *= 10
            c, tmp = str(tmp // denominator), tmp % denominator
            res.append(c)
            idx += 1
            if tmp in seen:
                break

        if tmp != 0:
            res.insert(seen[tmp], '(')
            res.append(')')
        return ''.join(res)