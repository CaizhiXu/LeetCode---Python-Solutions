## time, space - O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n < 0:
            raise Exception("Wrong input!")
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n%2 == 0:
            return (self.myPow(x, n/2))**2
        else:
            return x*(self.myPow(x, (n-1)/2))**2