## time, space - O(N**3)
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        memo = {}  ## memo[(i,j,k)] means the maximum value obtained with  this array: the first k nums equal boxes[i], followed by boxes[i:j+1]

        def helper(i, j, k):
            if j < i:
                return 0
            if (i, j, k) not in memo:
                m = i
                while m <= j and boxes[m] == boxes[i]:
                    m += 1
                ans = (k + m - i) ** 2 + helper(m, j, 0)
                tmp = boxes[i]
                for idx in range(m, j + 1):
                    if boxes[idx] == tmp:
                        ans = max(ans, helper(m, idx - 1, 0) + helper(idx, j, k + m - i))
                memo[(i, j, k)] = ans
            return memo[(i, j, k)]

        return helper(0, n - 1, 0)