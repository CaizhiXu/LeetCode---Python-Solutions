# time, space - O(N)
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flip = 0
        flip_mark = [0] * n
        cnt = 0

        for i in range(n):
            flip ^= flip_mark[i]
            if A[i] ^ flip == 0:
                if i + K > n:
                    return -1
                cnt += 1
                if i + K < n:
                    flip_mark[i + K] = 1
                flip ^= 1
        return cnt