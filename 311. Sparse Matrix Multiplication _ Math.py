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