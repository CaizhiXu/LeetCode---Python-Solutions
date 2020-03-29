## time - O(N*K), space - O(N)
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * len(A)

        currMax = 0
        for i in range(K):
            currMax = max(currMax, A[i])
            dp[i] = currMax * (i + 1)
        for i in range(K, len(A)):
            currMax = 0
            for j in range(K):
                currMax = max(currMax, A[i - j])
                dp[i] = max(dp[i], dp[i - 1 - j] + currMax * (j + 1))

        return dp[-1]