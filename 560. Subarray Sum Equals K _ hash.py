## time, space - O(N)
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = defaultdict(int)
        preSum[0] += 1
        currSum, res = 0, 0
        for num in nums:
            currSum += num
            if currSum-k in preSum:
                res += preSum[currSum-k]
            preSum[currSum] += 1
        return res