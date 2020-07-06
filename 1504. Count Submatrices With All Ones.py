## time - O(mmn), space - O(m)
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        cnt = 0

        m, n = len(mat), len(mat[0])
        for i in range(m):
            dp = [0] * (
                        i + 1)  ## dp[k] means the width of rectangles with (i,j) as the bottom right corner, and with height of k+1
            for j in range(n):
                zero_seen = False
                for k in range(i + 1):  ## check different hights
                    if mat[i - k][j] == 1 and not zero_seen:
                        dp[k] += 1  ## increase width by one
                        cnt += dp[k]
                    else:  ## if zero is seen along (i, j), (i-1, j), ... (0, j), the width becomes zero. The same for larger k.
                        zero_seen = True
                        dp[k] = 0
        return cnt