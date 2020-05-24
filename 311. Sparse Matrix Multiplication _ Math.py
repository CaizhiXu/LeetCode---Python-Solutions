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
class Solution2:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return []
        m, n = len(A), len(A[0])
        k = len(B[0])
        if n != len(B):
            raise ValueError("Dimension mismatch!")

        dictA = self.matrixDict(A)
        dictB = self.matrixDict(B)
        c = [[0] * k for i in range(m)]
        for i in range(m):
            for l, eleA in dictA[i].items():
                for j, eleB in dictB[l].items():
                    c[i][j] += eleA * eleB
        return c

    def matrixDict(self, matrix):
        dct = {}
        for i, row in enumerate(matrix):
            dct[i] = {}
            for j in range(len(row)):
                if row[j] != 0:
                    dct[i][j] = row[j]
        return dct