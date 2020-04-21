class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        sign = (dividend < 0) == (divisor < 0)
        if dividend > 0:
            dividend = - dividend
        if divisor > 0:
            divisor = - divisor

        res = 0
        while divisor >= dividend:
            count = 1
            tmp = divisor
            while tmp + tmp > dividend:
                count += count
                tmp += tmp
            res += count
            dividend -= tmp
        if sign:
            return res
        else:
            return -res