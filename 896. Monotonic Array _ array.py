## time - O(n), space - o(1)
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[0] == A[-1]:
            return all(num==A[0] for num in A)
        if A[0] < A[-1]:
            sign = 1
        else:
            sign = -1
        return all(sign*(A[i+1]-A[i])>=0 for i in range(len(A)-1))