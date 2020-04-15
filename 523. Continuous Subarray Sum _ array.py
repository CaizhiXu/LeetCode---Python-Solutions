## time - O(n), space - O(min(n, k))
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSum = 0
        bucket = defaultdict(list)
        bucket[0].append(-1)
        for i, num in enumerate(nums):
            preSum = preSum + num
            tmp = preSum
            if k != 0:
                tmp = tmp % k
            bucket[tmp].append(i)

        for key in bucket:
            lst = bucket[key]
            if lst[-1] - lst[0] >= 2:
                return True
        return False