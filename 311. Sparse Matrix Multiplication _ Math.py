## time - less than m*n*nB, space - m*nB
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        nB = len(B[0])
        C = [[0] * nB for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(nB):
                        if B[j][k] != 0:
                            C[i][k] += A[i][j] * B[j][k]

        return C


## time - less than m*n*nB, space - m*nB
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return None
        m, n = len(A), len(A[0])
        k = len(B[0])
        if len(B) != n:
            raise Exception("Dimension mismatch!")

        res = [[0] * k for i in range(m)]
        nonZero = {}
        for i, row in enumerate(B):
            nonZero[i] = {}
            for j in range(len(row)):
                if row[j] != 0:
                    nonZero[i][j] = row[j]
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA != 0:
                    for j, eleB in nonZero[k].items():
                        res[i][j] += eleA * eleB
        return res